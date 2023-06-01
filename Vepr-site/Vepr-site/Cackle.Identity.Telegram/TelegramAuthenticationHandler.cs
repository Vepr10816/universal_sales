using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Text;
using System.Text.Encodings.Web;
using System.Text.Json;
using System.Threading.Tasks;
using Cackle.Identity.Telegram.Internal;
using Microsoft.AspNetCore.Antiforgery;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.WebUtilities;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using Microsoft.Extensions.Primitives;
using Microsoft.Net.Http.Headers;
using static Cackle.Identity.Telegram.TelegramAuthenticationConstants;

namespace Cackle.Identity.Telegram
{
    public class TelegramAuthenticationHandler : RemoteAuthenticationHandler<TelegramAuthenticationOptions>
    {
        private readonly IAntiforgery _antiforgery;
        private readonly ISystemClock _clock;

        /// <summary>
        ///     Initializes a new instance of <see cref="TelegramAuthenticationHandler" />.
        /// </summary>
        /// <param name="options">The monitor for the options instance.</param>
        /// <param name="logger">The <see cref="ILoggerFactory" />.</param>
        /// <param name="encoder">The <see cref="UrlEncoder" />.</param>
        /// <param name="clock">The <see cref="ISystemClock" />.</param>
        /// <param name="antiforgery">The <see cref="IAntiforgery" />.</param>
        public TelegramAuthenticationHandler(IOptionsMonitor<TelegramAuthenticationOptions> options,
            ILoggerFactory logger, UrlEncoder encoder, ISystemClock clock, IAntiforgery antiforgery) : base(options,
            logger, encoder, clock)
        {
            _clock = clock;
            _antiforgery = antiforgery;
        }

        /// <inheritdoc />
        protected override async Task<HandleRequestResult> HandleRemoteAuthenticateAsync()
        {
            if (!await _antiforgery.IsRequestValidAsync(Context))
                return HandleRequestResult.Fail("Antiforgery validation failed.");

            var state = Request.Query["state"];
            var properties = Options.StateDataFormat.Unprotect(state);

           /* if (!ValidateCorrelationId(properties!))
                return HandleRequestResult.Fail("Correlation failed.", properties);

            if (Options.AllowedOrigins != null)
            {*/
               // var origin = new Uri(Request.Form[Options.OriginFieldName].First());
                /*if (!Options.AllowedOrigins.Any(x => x.Scheme.Equals(origin.Scheme) && x.Host.Equals(origin.Host)))
                {
                    Logger.LogInformation("Origin provided is not allowed.");
                    return HandleRequestResult.Fail("Verification failed.", properties);
                }
            }*/

            var userData = DecodeUserData(Request.Form);

            //HttpContext.Session.SetObjectAsJson("UserData", userData);

            if (!long.TryParse(userData[DataCheckKeys.AuthTime], out var longAuthTime))
            {
                Logger.LogInformation("Authorization time not found.");
                return HandleRequestResult.Fail("Verification failed.", properties);
            }

            var authTime = DateTimeOffset.FromUnixTimeSeconds(longAuthTime);
            if (authTime + TimeSpan.FromMinutes(-5) > _clock.UtcNow ||
                authTime + TimeSpan.FromMinutes(5) < _clock.UtcNow)
            {
                Logger.LogInformation("Time provided by is not without an acceptable range.");
                return HandleRequestResult.Fail("Verification failed.", properties);
            }

            var generatedHash = GenerateHash(userData);
            if (!generatedHash.Equals(userData[DataCheckKeys.AuthHash]))
            {
                Logger.LogInformation("Hash verification failed.");
                return HandleRequestResult.Fail("Verification failed.", properties);
            }

           /* properties.IssuedUtc = authTime;

            if (Options.ExpiryMinutes > 0)
                properties.ExpiresUtc = _clock.UtcNow + TimeSpan.FromMinutes(Options.ExpiryMinutes);*/

            var identity = new ClaimsIdentity(TelegramAuthenticationDefaults.ClaimsIssuer);
            var ticket = CreateTicket(identity, properties, userData);

            return ticket == null ? HandleRequestResult.Fail("Failed") : HandleRequestResult.Success(ticket);
        }

        /// <inheritdoc />
        protected override Task HandleChallengeAsync(AuthenticationProperties properties)
        {
            if (string.IsNullOrEmpty(properties.RedirectUri))
                properties.RedirectUri = OriginalPathBase + OriginalPath + Request.QueryString;

            GenerateCorrelationId(properties);

            var parameters = new Dictionary<string, string>
            {
                {"redirectUri", BuildRedirectUri(Options.CallbackPath)},
                {"state", Options.StateDataFormat.Protect(properties)}
            };

            var authorizationEndpoint = QueryHelpers.AddQueryString(Options.AuthorizationEndpoint, parameters);
            Response.Redirect(authorizationEndpoint);

            var location = Context.Response.Headers[HeaderNames.Location];
            if (location == StringValues.Empty) location = "(not set)";

            var cookie = Context.Response.Headers[HeaderNames.SetCookie];
            if (cookie == StringValues.Empty) cookie = "(not set)";

            Logger.LogDebug("HandleChallenge with Location: {Location}; and Set-Cookie: {Cookie}.", location, cookie);

            return Task.CompletedTask;
        }

        /// <summary>
        ///     Creates claims for the provided data from Telegram.
        /// </summary>
        /// <param name="identity"><inheritdoc cref="ClaimsIdentity" />.</param>
        /// <param name="properties"><inheritdoc cref="AuthenticationProperties" />.</param>
        /// <param name="userData">Key/value pairs of Telegram provided user data.</param>
        /// <returns>An authentication ticket.</returns>
        public AuthenticationTicket CreateTicket(ClaimsIdentity identity, AuthenticationProperties properties,
            IDictionary<string, string> userData)
        {
            var name = userData[DataCheckKeys.FirstName];
            if (userData.TryGetValue(DataCheckKeys.LastName, out var lastName))
            {
                name = string.Concat(name, (char) 0x20, lastName);
                identity.AddClaim(new Claim(Claims.LastName, lastName));
            }

            identity.AddClaims(new Claim[]
            {
                new(ClaimTypes.NameIdentifier, userData[DataCheckKeys.Id]),
                new(ClaimTypes.Name, name),
                new(Claims.FirstName, userData[DataCheckKeys.FirstName])
            });

            if (userData.TryGetValue(DataCheckKeys.UserName, out var userName))
                identity.AddClaim(new Claim(Claims.UserName, userName));

            if (userData.TryGetValue(DataCheckKeys.PhotoUrl, out var photoUrl))
                identity.AddClaim(new Claim(Claims.PhotoUrl, photoUrl));

            var principal = new ClaimsPrincipal(identity);
            return new AuthenticationTicket(principal, properties, Scheme.Name);
        }

        /// <summary>
        ///     Decode from base64 User Data submitted by a form.
        /// </summary>
        /// <param name="form"><inheritdoc cref="IFormCollection" />.</param>
        /// <returns>Key/value pairs of user data provided by Telegram.</returns>
        private IDictionary<string, string> DecodeUserData(IFormCollection form)
        {
            var data = form[Options.UserDataFieldName].First();
            var json = Encoding.UTF8.GetString(Convert.FromBase64String(data));

            var options = new JsonSerializerOptions {Converters = {new DictionaryStringJsonConverter()}};
            return JsonSerializer.Deserialize<IDictionary<string, string>>(json, options);
        }

        /// <summary>
        ///     Generates a hash as mentioned in <see href="https://core.telegram.org/widgets/login">Telegram Login Widget</see>
        ///     documentation.
        /// </summary>
        /// <param name="data">Key/value pairs of user data.</param>
        /// <returns>Hash of key/value pairs to validate against Telegram provided hash.</returns>
        private string GenerateHash(IDictionary<string, string> data)
        {
            var components = data
                .Where(x => !x.Key.Equals(DataCheckKeys.AuthHash))
                .OrderBy(x => x.Key)
                .Select(x => string.Concat(x.Key, (char) 0x3d, x.Value));

            var dataCheckString = string.Join((char) 0x0a, components);

            byte[] key;
            using (var sha = SHA256.Create())
            {
                key = sha.ComputeHash(Encoding.UTF8.GetBytes(Options.ApiToken));
            }

            byte[] hash;
            using (var hmac = new HMACSHA256(key))
            {
                hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(dataCheckString));
            }

            var result = new StringBuilder();
            foreach (var b in hash) result.Append(b.ToString("x2"));
            return result.ToString();
        }
    }
}
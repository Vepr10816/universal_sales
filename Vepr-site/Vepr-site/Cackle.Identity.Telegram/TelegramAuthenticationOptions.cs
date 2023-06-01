using System;
using Microsoft.AspNetCore.Authentication;

namespace Cackle.Identity.Telegram
{
    /// <summary>
    ///     Contains options used by <see cref="TelegramAuthenticationHandler" />
    /// </summary>
    public class TelegramAuthenticationOptions : RemoteAuthenticationOptions
    {
        /// <summary>
        ///     Initialized a new <see cref="TelegramAuthenticationOptions" />
        /// </summary>
        public TelegramAuthenticationOptions()
        {
            AuthorizationEndpoint = TelegramAuthenticationDefaults.AuthorizationEndpoint;
            CallbackPath = TelegramAuthenticationDefaults.CallbackPath;
            OriginFieldName = TelegramAuthenticationDefaults.OriginFieldName;
            UserDataFieldName = TelegramAuthenticationDefaults.UserDataFieldName;
        }

        /// <inheritdoc cref="Microsoft.AspNetCore.Authentication.OAuth.OAuthOptions.AuthorizationEndpoint" />
        public string AuthorizationEndpoint { get; set; }

        /// <summary>
        ///     Telegram API Token.
        /// </summary>
        public string ApiToken { get; set; }

        /// <summary>
        ///     Optional allowed origins provided by Telegram API. Both the host and scheme must match. Although this adds an
        ///     additional layer of protection, it can be easily spoofed due to this data being intercepted by the end user's
        ///     browser.
        /// </summary>
        public Uri[] AllowedOrigins { get; set; }

        /// <summary>
        ///     Optional length of time in minutes before claims ticket expires. If none specified, the ticket does not expire. Due
        ///     to the inability to automatically refresh tokens from Telegram, it is highly recommended provide an appropriate
        ///     length of time.
        /// </summary>
        public int ExpiryMinutes { get; set; }

        /// <summary>
        ///     The name of the form field used to receive origin.
        /// </summary>
        public string OriginFieldName { get; set; }

        /// <summary>
        ///     The name of the form field used to receive user data.
        /// </summary>
        public string UserDataFieldName { get; set; }

        /// <inheritdoc cref="Microsoft.AspNetCore.Authentication.OAuth.OAuthOptions.StateDataFormat" />
        public ISecureDataFormat<AuthenticationProperties> StateDataFormat { get; set; }

        /// <inheritdoc cref="Microsoft.AspNetCore.Authentication.RemoteAuthenticationOptions.Validate()" />
        public override void Validate()
        {
            base.Validate();

            if (string.IsNullOrEmpty(ApiToken))
                throw new ArgumentException("Telegram API token must be provided", nameof(ApiToken));

            if (string.IsNullOrEmpty(AuthorizationEndpoint))
                throw new ArgumentException("Authorization endpoint token must be provided",
                    nameof(AuthorizationEndpoint));
        }
    }
}
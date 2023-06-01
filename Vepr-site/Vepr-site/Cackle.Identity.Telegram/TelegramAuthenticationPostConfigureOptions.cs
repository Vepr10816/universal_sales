using System;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.DataProtection;
using Microsoft.Extensions.Options;

namespace Cackle.Identity.Telegram
{
    /// <summary>
    ///     Configure defaults for <see cref="TelegramAuthenticationOptions" />
    /// </summary>
    public class TelegramAuthenticationPostConfigureOptions : IPostConfigureOptions<TelegramAuthenticationOptions>
    {
        private readonly IDataProtectionProvider _dataProtection;

        /// <summary>
        ///     Initializes <see cref="TelegramAuthenticationPostConfigureOptions" />.
        /// </summary>
        /// <param name="dataProtection">The <see cref="IDataProtectionProvider" />.</param>
        public TelegramAuthenticationPostConfigureOptions(IDataProtectionProvider dataProtection)
        {
            _dataProtection = dataProtection;
        }

        /// <inheritdoc />
        public void PostConfigure(string name, TelegramAuthenticationOptions options)
        {
            options.DataProtectionProvider ??= _dataProtection;

            if (options.DataProtectionProvider == null)
                throw new ArgumentNullException(nameof(options.DataProtectionProvider),
                    "Data Protection Provider not configured");

            if (options.StateDataFormat != null) return;

            var dataProtector =
                options.DataProtectionProvider.CreateProtector(typeof(TelegramAuthenticationHandler).FullName!, name);
            options.StateDataFormat = new PropertiesDataFormat(dataProtector);
        }
    }
}
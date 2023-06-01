using System;
using Cackle.Identity.Telegram;
using Microsoft.AspNetCore.Authentication;
using Microsoft.Extensions.Options;

namespace Microsoft.Extensions.DependencyInjection
{
    public static class TelegramAuthenticationBuilder
    {
        /// <summary>
        ///     Adds Telegram Authentication to .NET Identity.
        /// </summary>
        /// <param name="builder">The authentication builder.</param>
        /// <param name="configureOptions">Delegate to configure <see cref="TelegramAuthenticationOptions" />.</param>
        /// <returns>A reference to this instance after the operation has completed.</returns>
        public static AuthenticationBuilder AddTelegram(this AuthenticationBuilder builder,
            Action<TelegramAuthenticationOptions> configureOptions)
        {
            builder.Services
                .AddSingleton<IPostConfigureOptions<TelegramAuthenticationOptions>,
                    TelegramAuthenticationPostConfigureOptions>();

            builder.AddScheme<TelegramAuthenticationOptions, TelegramAuthenticationHandler>(
                TelegramAuthenticationDefaults.Name, TelegramAuthenticationDefaults.DisplayName, configureOptions);

            return builder;
        }
    }
}
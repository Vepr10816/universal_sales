using System;
using Cackle.Identity.Telegram.UI;
using Microsoft.AspNetCore.Authentication;

namespace Microsoft.Extensions.DependencyInjection
{
    public static class TelegramLoginWidgetExtensions
    {
        /// <summary>
        ///     Customizes the Telegram Login Widget. The <see cref="TelegramLoginWidgetOptions.CallbackPath" /> must be defined.
        /// </summary>
        /// <param name="builder">The authentication builder.</param>
        /// <param name="configureOptions">Delegate to configure <see cref="TelegramLoginWidgetOptions" />.</param>
        /// <returns>A reference to this instance after the operation has completed.</returns>
        public static AuthenticationBuilder AddTelegramUI(this AuthenticationBuilder builder,
            Action<TelegramLoginWidgetOptions> configureOptions)
        {
            builder.Services.Configure(configureOptions);
            return builder;
        }

        /// <summary>
        ///     Customizes the Telegram Login Widget. The <see cref="TelegramLoginWidgetOptions.CallbackPath" /> must be defined.
        /// </summary>
        /// <param name="services">The service collection.</param>
        /// <param name="configureOptions">Delegate to configure <see cref="TelegramLoginWidgetOptions" />.</param>
        /// <returns>A reference to this instance after the operation has completed.</returns>
        public static IServiceCollection AddTelegramUI(this IServiceCollection services,
            Action<TelegramLoginWidgetOptions> configureOptions)
        {
            services.Configure(configureOptions);
            return services;
        }
    }
}
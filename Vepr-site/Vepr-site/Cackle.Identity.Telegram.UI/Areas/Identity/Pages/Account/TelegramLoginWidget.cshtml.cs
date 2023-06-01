using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Cackle.Identity.Telegram.UI.Areas.Identity.Pages.Account
{
    public class TelegramLoginWidgetModel : PageModel
    {
        public readonly string BotUserName;
        public readonly string ButtonStyle;
        public readonly string CallbackPath;
        public readonly int CornerRadius;
        public readonly string RedirectUrl;
        public readonly bool SendMessageAccess;
        public readonly bool ShowUserPhoto;

        /// <summary>
        ///     Configures <paramref cref="TelegramLoginWidgetOptions" />
        /// </summary>
        /// <param name="botUserName">
        ///     <inheritdoc cref="TelegramLoginWidgetOptions.BotUserName" />
        /// </param>
        /// <param name="callbackPath">
        ///     <inheritdoc cref="TelegramLoginWidgetOptions.CallbackPath" />
        /// </param>
        /// <param name="buttonStyle">
        ///     <inheritdoc cref="TelegramLoginWidgetOptions.ButtonStyle" />
        /// </param>
        /// <param name="showUserPhoto">
        ///     <inheritdoc cref="TelegramLoginWidgetOptions.ShowUserPhoto" />
        /// </param>
        /// <param name="cornerRadius">
        ///     <inheritdoc cref="TelegramLoginWidgetOptions.CornerRadius" />
        /// </param>
        /// <param name="redirectUrl">
        ///     <inheritdoc cref="TelegramLoginWidgetOptions.RedirectUrl" />
        /// </param>
        /// <param name="sendMessageAccess">
        ///     <inheritdoc cref="TelegramLoginWidgetOptions.SendMessageAccess" />
        /// </param>
        public TelegramLoginWidgetModel(string botUserName,
            string callbackPath = TelegramLoginWidgetDefaults.CallbackPath,
            string buttonStyle = TelegramLoginWidgetDefaults.ButtonStyle,
            bool showUserPhoto = TelegramLoginWidgetDefaults.ShowUserPhoto,
            int cornerRadius = TelegramLoginWidgetDefaults.CornerRadius,
            string redirectUrl = TelegramLoginWidgetDefaults.RedirectUrl,
            bool sendMessageAccess = TelegramLoginWidgetDefaults.SendMessageAccess)
        {
            BotUserName = botUserName;
            CallbackPath = callbackPath;
            ButtonStyle = buttonStyle;
            ShowUserPhoto = showUserPhoto;
            CornerRadius = cornerRadius;
            RedirectUrl = redirectUrl;
            SendMessageAccess = sendMessageAccess;
        }

        /// <summary>
        ///     Configures <paramref cref="TelegramLoginWidgetOptions" />
        /// </summary>
        /// <param name="widgetOptions">Allows manually configuring the Telegram Login widget.</param>
        public TelegramLoginWidgetModel(TelegramLoginWidgetOptions widgetOptions)
        {
            BotUserName = widgetOptions.BotUserName;
            CallbackPath = widgetOptions.CallbackPath;
            ButtonStyle = widgetOptions.ButtonStyle;
            ShowUserPhoto = widgetOptions.ShowUserPhoto;
            CornerRadius = widgetOptions.CornerRadius;
            RedirectUrl = widgetOptions.RedirectUrl;
            SendMessageAccess = widgetOptions.SendMessageAccess;
        }

        /// <summary>
        ///     Convenience method to configure model.
        /// </summary>
        /// <param name="widgetOptions" />
        /// <returns>An instance of this object.</returns>
        public static TelegramLoginWidgetModel Configure(TelegramLoginWidgetOptions widgetOptions)
        {
            return new(widgetOptions);
        }
    }
}
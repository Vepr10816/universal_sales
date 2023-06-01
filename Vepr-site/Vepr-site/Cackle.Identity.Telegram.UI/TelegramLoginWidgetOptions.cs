namespace Cackle.Identity.Telegram.UI
{
    public class TelegramLoginWidgetOptions
    {
        /// <summary>
        ///     A required field. Specifies the user name of the bot used in the Telegram Login Widget. See
        ///     <see href="https://core.telegram.org/widgets/login">Telegram Login Widget</see>.
        /// </summary>
        public string BotUserName { get; set; }

        /// <summary>
        ///     Specifies the size of the button in the Telegram Login Widget. See
        ///     <see href="https://core.telegram.org/widgets/login">Telegram Login Widget</see>.
        /// </summary>
        public string ButtonStyle { get; set; } = TelegramLoginWidgetDefaults.ButtonStyle;

        /// <summary>
        ///     The path used in the the built-in, hidden form on the Telegram Login Widget page.
        /// </summary>
        public string CallbackPath { get; set; } = TelegramLoginWidgetDefaults.CallbackPath;

        /// <summary>
        ///     The corner radius of the button in the Telegram Login Widget. See
        ///     <see href="https://core.telegram.org/widgets/login">Telegram Login Widget</see>.
        /// </summary>
        public int CornerRadius { get; set; } = TelegramLoginWidgetDefaults.CornerRadius;

        /// <summary>
        ///     If specified, directs the Telegram Login Widget to redirect the page rather than use the built-in JavaScript. By
        ///     default, the Telegram Login Widget uses a hidden form which submits user data via <see cref="CallbackPath" />.
        /// </summary>
        public string RedirectUrl { get; set; } = TelegramLoginWidgetDefaults.RedirectUrl;

        /// <summary>
        ///     Allows end-users to send messages from your bot. See
        ///     <see href="https://core.telegram.org/widgets/login">Telegram Login Widget</see>.
        /// </summary>
        public bool SendMessageAccess { get; set; } = TelegramLoginWidgetDefaults.SendMessageAccess;

        /// <summary>
        ///     Shows the end-user photo next to the Telegram login button if a Telegram cookie already exists in their browser.
        ///     See <see href="https://core.telegram.org/widgets/login">Telegram Login Widget</see>.
        /// </summary>
        public bool ShowUserPhoto { get; set; } = TelegramLoginWidgetDefaults.ShowUserPhoto;
    }
}
namespace Cackle.Identity.Telegram.UI
{
    public static class TelegramLoginWidgetDefaults
    {
        /// <summary>
        ///     Default path used in hidden login form. "/signin-telegram" is the default CallbackPath in Cackle.Identity.Telegram.
        /// </summary>
        public const string CallbackPath = "/Index";

        /// <summary>
        ///     The default size of the Telegram Login Widget.
        /// </summary>
        public const string ButtonStyle = "large";

        /// <summary>
        ///     The default corner radius of the Telegram Login Widget. Setting to -1 allows the Telegram Login Widget to
        ///     automatically choose rounded corners.
        /// </summary>
        public const int CornerRadius = -1;

        /// <summary>
        ///     By default the Telegram Login Widget does not use RedirectUrl, instead using JavaScript built into the page.
        /// </summary>
        public const string RedirectUrl = "";

        /// <summary>
        ///     By default the Telegram Login Widget allows users to send messages from your bot.
        /// </summary>
        public const bool SendMessageAccess = true;

        /// <summary>
        ///     The default option shows the user's photo next to the Login Widget.
        /// </summary>
        public const bool ShowUserPhoto = true;
    }
}
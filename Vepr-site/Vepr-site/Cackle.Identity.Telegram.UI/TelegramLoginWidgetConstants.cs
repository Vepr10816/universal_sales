namespace Cackle.Identity.Telegram.UI
{
    public static class TelegramLoginWidgetConstants
    {
        /// <summary>
        ///     The Origin form field name built into the Telegram Login Widget. This name is also required to be set on the
        ///     receiving party. The Origin field is populated by JavaScript on the Telegram Login Widget page and is derived from
        ///     Telegram.
        /// </summary>
        public const string OriginField = "__tgOrigin";

        /// <summary>
        ///     The User Data form field name built into the Telegram Login Widget. This name is also required to be set on the
        ///     receiving party. The Origin field is populated by JavaScript on the Telegram Login Widget page and is provided by
        ///     Telegram via JavaScript.
        /// </summary>
        public const string UserDataField = "__tgUserData";
    }
}
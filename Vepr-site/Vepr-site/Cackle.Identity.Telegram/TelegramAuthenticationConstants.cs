namespace Cackle.Identity.Telegram
{
    public static class TelegramAuthenticationConstants
    {
        /// <summary>
        ///     Key names to the key/value pairs provided by Telegram during authentication.
        /// </summary>
        public static class DataCheckKeys
        {
            /// <summary>
            ///     Key of key/value pair for the instant Telegram authenticated user.
            /// </summary>
            public const string AuthTime = "auth_date";

            /// <summary>
            ///     Key of key/value pair for Telegram calculated hash using API key as secret.
            /// </summary>
            public const string AuthHash = "hash";

            /// <summary>
            ///     Key of key/value pair for Telegram user's first name.
            /// </summary>
            public const string FirstName = "first_name";

            /// <summary>
            ///     Key of key/value pair for Telegram user's ID.
            /// </summary>
            public const string Id = "id";

            /// <summary>
            ///     Optional key of key/value pair for Telegram user's last name.
            /// </summary>
            public const string LastName = "last_name";

            /// <summary>
            ///     Optional key of key/value pair for a URL to user's photo.
            /// </summary>
            public const string PhotoUrl = "photo_url";

            /// <summary>
            ///     Optional key of key/value pair for user's user name.
            /// </summary>
            public const string UserName = "username";
        }

        /// <summary>
        ///     Telegram provided data.
        /// </summary>
        public static class Claims
        {
            /// <summary>
            ///     Telegram user's first name.
            /// </summary>
            public const string FirstName = "urn:telegram:first_name";

            /// <summary>
            ///     Optional Telegram user's last name.
            /// </summary>
            public const string LastName = "urn:telegram:last_name";

            /// <summary>
            ///     Optional Telegram user's user name.
            /// </summary>
            public const string UserName = "urn:telegram:user_name";

            /// <summary>
            ///     Optional Telegram user's photo.
            /// </summary>
            public const string PhotoUrl = "urn:telegram:avatar:url";
        }
    }
}
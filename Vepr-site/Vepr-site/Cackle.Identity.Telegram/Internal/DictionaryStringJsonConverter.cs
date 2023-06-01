using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Cackle.Identity.Telegram.Internal
{
    /// <summary>
    ///     Provides the ability to to convert JSON key/value pairs to a <type name="IDictionary" />.
    /// </summary>
    internal class DictionaryStringJsonConverter : JsonConverter<IDictionary<string, string>>
    {
        public override IDictionary<string, string> Read(ref Utf8JsonReader reader, Type typeToConvert,
            JsonSerializerOptions options)
        {
            var dictionary = new Dictionary<string, string>();

            while (reader.Read())
            {
                if (reader.TokenType == JsonTokenType.EndObject) return dictionary;

                if (reader.TokenType != JsonTokenType.PropertyName)
                    throw new JsonException("Did not encounter PropertyName");

                var propertyName = reader.GetString();

                if (string.IsNullOrWhiteSpace(propertyName))
                    throw new JsonException("Failed to get property name");

                reader.Read();

                var propertyValue = ExtractString(ref reader);

                if (!string.IsNullOrWhiteSpace(propertyValue))
                    dictionary.Add(propertyName, propertyValue);
            }

            return dictionary;
        }

        public override void Write(Utf8JsonWriter writer, IDictionary<string, string> value,
            JsonSerializerOptions options)
        {
            JsonSerializer.Serialize(writer, value, options);
        }

        private static string ExtractString(ref Utf8JsonReader reader)
        {
            switch (reader.TokenType)
            {
                case JsonTokenType.String:
                    return reader.GetString();

                case JsonTokenType.Number:
                    if (reader.TryGetInt64(out var result)) return result.ToString();
                    else if (reader.TryGetDecimal(out var d)) return d.ToString("N");
                    throw new JsonException("Unable to convert to string");

                case JsonTokenType.True:
                    return $"{true}";

                case JsonTokenType.False:
                    return $"{false}";

                case JsonTokenType.Null:
                    return null;

                default:
                    throw new JsonException($"'{reader.TokenType}' is not supported");
            }
        }
    }
}
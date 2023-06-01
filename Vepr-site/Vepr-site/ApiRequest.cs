using RestSharp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site
{
    /// <summary>
    /// Обработка запросов к API.
    /// </summary>
    public class ApiRequest
    {
        private readonly RestClient _client;

        /// <summary>
        /// Экземпляр домена к API.
        /// </summary>
        /// <param name="baseUrl">Домен.</param>
        public ApiRequest(string baseUrl = "http://vepr_backend:6200")
        {
            _client = new RestClient(baseUrl);
        }

        /// <summary>
        /// Отправка Get запроса.
        /// </summary>
        /// <param name="url">Строка запроса.</param>
        /// <returns>Ответ API.</returns>
        public RestResponse Get(string url)
        {
            return TryExecute(() => _client.Get(new RestRequest(url)));
        }

        /// <summary>
        /// Отправка Post запроса.
        /// </summary>
        /// <param name="url">Строка запроса.</param>
        /// <returns>Ответ API.</returns>
        public RestResponse Post(string url)
        {
            return TryExecute(() => _client.Post(new RestRequest(url)));
        }

        /// <summary>
        /// Отправка Post запроса с токеном пользователя.
        /// </summary>
        /// <param name="url">Строка запроса.</param>
        /// <returns>Ответ API.</returns>
        public void Post(string url, string bearer)
        {

            var request = new RestRequest(url);
            request.AddHeader("Authorization", $"Bearer {bearer}");
            TryExecute(() => _client.Post(request));

        }

        /// <summary>
        /// Отправка Put запроса с токеном пользователя.
        /// </summary>
        /// <param name="url">Строка запроса.</param>
        /// <returns>Ответ API.</returns>
        public void Put(string url)
        {
            TryExecute(() => _client.Put(new RestRequest(url)));
        }

        /// <summary>
        /// Обработка ошибочных запросов.
        /// </summary>
        /// <param name="action">Выполненное действие.</param>
        /// <returns>Ошибка.</returns>
        private static RestResponse TryExecute(Func<RestResponse> action)
        {
            try
            {
                return action();
            }
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine(e.Message);
                return null;
            }
        }
    }
}

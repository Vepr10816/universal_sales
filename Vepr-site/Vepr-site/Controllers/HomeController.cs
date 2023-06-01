using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Vepr_site.Models;
using Flurl.Http;
using RestSharp;
using Newtonsoft.Json;
using System.Security.Claims;
using System.IO;

namespace Vepr_site.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        /// <summary>
        /// Показ стрница о разработчике.
        /// </summary>
        /// <returns>Стрница о разработчике.</returns>
        public IActionResult Privacy()
        {
            return View();
        }

        /// <summary>
        /// Обработка ошибок.
        /// </summary>
        /// <returns>Страница об шибке.</returns>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

        /// <summary>
        /// Показ основной страницы сайта.
        /// </summary>
        /// <returns>Основная страница сайта.</returns>
        public IActionResult Index()
        {
            var response = new ApiRequest().Get("allCategoryFromUser/1");
            List<Category> categoryList = JsonConvert.DeserializeObject<List<Category>>(response.Content);
            HttpContext.Session.SetObjectAsJson("CategoryList", categoryList);
            return View(new Company
            {
                MyCompany = JsonConvert.DeserializeObject<MyCompany>((new ApiRequest().Get("myCompany")).Content),
                Addresses = JsonConvert.DeserializeObject<List<Address>>((new ApiRequest().Get("allAddresses/1")).Content),
                Requisites = JsonConvert.DeserializeObject<List<Requisites>>((new ApiRequest().Get("allRequisites/1")).Content)
            });
        }

        /// <summary>
        /// Обработка логгера.
        /// </summary>
        /// <param name="obj">объект логера</param>
        /// <returns>логгер</returns>
        public override bool Equals(object obj)
        {
            return obj is HomeController controller &&
                   EqualityComparer<ILogger<HomeController>>.Default.Equals(_logger, controller._logger);
        }

       
        public override int GetHashCode()
        {
            throw new NotImplementedException();
        }
    }
}

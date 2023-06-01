using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using RestSharp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;
using Vepr_site.Models;

namespace Vepr_site.Controllers
{
    /// <summary>
    /// Контроллер формирования заказа.
    /// </summary>
    public class OrderController : Controller
    {
        /// <summary>
        /// Вывод cтраницы о успешном оформлении заказа.
        /// </summary>
        /// <returns>cтраница о успешном оформлении заказа.</returns>
        public IActionResult Index()
        {
            List<Basket> basket = HttpContext.Session.GetObjectFromJson<List<Basket>>("Basket");
            string url = "order?";
            string urlIdProductList = "";
            string urlQuantityList = "";
            double totalPrice = 0;
            string urlIdProductCharacteristicsList = "";
            if(basket != null)
            {
                foreach(var item in basket)
                {
                    urlIdProductList += $@"idProductList={item.Product.ID}&";
                    urlQuantityList += $@"quantityList={item.Quantity}&";
                    totalPrice += item.Price;
                    foreach(int idCharacteristic in item.IDProductCharacteristicsList)
                    {
                        urlIdProductCharacteristicsList += $@"&idProductCharacteristicsList={idCharacteristic}";
                    }
                }
                string urlTotalPrice = $@"totalPrice={totalPrice}&comment=" + "\"-\"";
                url = url + urlIdProductList + urlQuantityList + urlTotalPrice + urlIdProductCharacteristicsList;

                System.Security.Claims.ClaimsPrincipal currentUser = this.User;

                new ApiRequest().Put($@"token?tgID={currentUser.FindFirst(ClaimTypes.NameIdentifier).Value}&idRole=2");

                
                var response = new ApiRequest().Get($@"token?tgID={currentUser.FindFirst(ClaimTypes.NameIdentifier).Value}");
                var apiAnswer = JsonConvert.DeserializeObject<ApiAnswer>(response.Content);

                try
                {
                    new ApiRequest().Post(url, apiAnswer.Data.RefreshToken);
                    HttpContext.Session.SetObjectAsJson("Basket", null);
                    HttpContext.Session.SetObjectAsJson("BasketCount", 0);
                    ViewBag.Message = $@"{currentUser.Identity.Name}, 
                                         спасибо за оставленный заказ. В ближайшее время с вами свяжется наш сотрудник. 
                                         Для просмотра статуса заказов и их отмены воспользуйтесь услугами Telegram бота:";
                    ViewBag.TelegramUrl = "https://web.telegram.org/a/#5174124946";
                }
                catch
                {
                    ViewBag.Message = "Ошибка сервера. В ближайшее время сервис восстановится.";
                }
            }
            else
            {
                ViewBag.Message = "Корзина пуста";
            }
            return View();
        }
    }
}

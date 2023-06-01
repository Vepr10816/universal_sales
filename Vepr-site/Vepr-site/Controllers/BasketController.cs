using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Vepr_site.Models;

namespace Vepr_site.Controllers
{
    /// <summary>
    /// Контроллер корзины.
    /// </summary>
    public class BasketController : Controller
    {
        /// <summary>
        /// Основная страница корзины.
        /// </summary>
        /// <returns>Представление страницы корзины.</returns>
        public IActionResult Index()
        {
            List<Basket> basket = HttpContext.Session.GetObjectFromJson<List<Basket>>("Basket");
            if (basket == null)
                basket = new List<Basket>();
            return View(basket);
        }

        /// <summary>
        /// Перенаправление на страницу товара.
        /// </summary>
        /// <param name="idProduct">первичный ключ товара.</param>
        /// <returns>Представление страницы товара.</returns>
        [HttpGet]
        public ActionResult RedirectToSelectedProduct(int idProduct)
        {
            HttpContext.Session.SetObjectAsJson("IDProduct", idProduct);
            return RedirectToAction("Index", "SelectedProduct");
        }

        /// <summary>
        /// Уменьшение количества товара.
        /// </summary>
        /// <param name="idBasket">Первичный ключ корзины.</param>
        /// <returns>Новое представление странцы корзины.</returns>
        [HttpGet]
        public ActionResult ChangeQuantityMinus(int idBasket)
        {
            List<Basket> basket = HttpContext.Session.GetObjectFromJson<List<Basket>>("Basket");
            if(basket[idBasket].Quantity > 1)
                basket[idBasket].Quantity -= 1;
            HttpContext.Session.SetObjectAsJson("Basket", basket);
            return RedirectToAction("Index", "Basket");
        }

        /// <summary>
        /// Увелечение количества товара.
        /// </summary>
        /// <param name="idBasket">Первичный ключ корзины.</param>
        /// <returns>Новое представление странцы корзины.</returns>
        [HttpGet]
        public ActionResult ChangeQuantityPlus(int idBasket)
        {
            List<Basket> basket = HttpContext.Session.GetObjectFromJson<List<Basket>>("Basket");
            basket[idBasket].Quantity += 1;
            HttpContext.Session.SetObjectAsJson("Basket", basket);
            return RedirectToAction("Index", "Basket");
        }

        /// <summary>
        /// Удаление товара из корзины.
        /// </summary>
        /// <param name="idBasket">Первичный ключ корзины.</param>
        /// <returns>Новое представление странцы корзины.</returns>
        [HttpGet]
        public ActionResult DeleteProduct(int idBasket)
        {
            List<Basket> basket = HttpContext.Session.GetObjectFromJson<List<Basket>>("Basket");
            basket.RemoveAt(idBasket);
            HttpContext.Session.SetObjectAsJson("Basket", basket);
            return RedirectToAction("Index", "Basket");
        }
    }
}

using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using RestSharp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Vepr_site.Models;

namespace Vepr_site.Controllers
{
    /// <summary>
    /// Контроллер для страницы выбранного товара.
    /// </summary>
    public class SelectedProductController : Controller
    {
        /// <summary>
        /// Отображение страницы товара и информации о нем.
        /// Заполнение модели отсортированными данными.
        /// </summary>
        /// <returns>Страница товара.</returns>
        [HttpGet]
        public IActionResult Index()
        {
            int idProduct = HttpContext.Session.GetObjectFromJson<int>("IDProduct");
            var response = new ApiRequest().Get($@"product/{idProduct}");
            Product product = JsonConvert.DeserializeObject<Product>(response.Content);
            try
            {
                Product productContainer = JsonConvert.DeserializeObject<Product>(response.Content);
                response = new ApiRequest().Get($@"allCharacteristics/{product.Subcategory.ID}");
                List<Characteristics> characteristicsList = JsonConvert.DeserializeObject<List<Characteristics>>(response.Content);
                foreach (var characteristic in characteristicsList)
                {
                    for (int i = 0; i < product.ProductCharacteristicsList.Count; i++)
                    {
                        if (characteristic.ID == product.ProductCharacteristicsList[i].Characteristics.ID)
                        {
                            productContainer.ProductCharacteristicsList[i].Characteristics = characteristic;
                        }
                    }
                }

                var evalVM = new Evaluation();
                int idCharacteristic = 0;
                var q1 = new Question();
                var productCharacteristicsList = productContainer.ProductCharacteristicsList
                    .Where(x => x.Characteristics.Selectable &&
                        productContainer.ProductCharacteristicsList.Count(y => y.Characteristics.ID == x.Characteristics.ID) > 1)
                    .ToList();
                for (int i = 0; i < productCharacteristicsList.Count; i++)
                {
                    var characteristic = productCharacteristicsList[i];

                    if (characteristic.Characteristics.ID == idCharacteristic)
                    {
                        q1.Answers.Add(new Answer
                        {
                            ID = characteristic.ID,
                            AnswerText = characteristic.CharacteristcValue
                        });

                        if (i == productCharacteristicsList.Count - 1 ||
                            characteristic.Characteristics.ID != productContainer.ProductCharacteristicsList[i + 1].Characteristics.ID)
                        {
                            evalVM.Questions.Add(q1);
                        }
                    }
                    else
                    {
                        q1 = new Question
                        {
                            ID = characteristic.Characteristics.ID,
                            QuestionText = characteristic.Characteristics.CharacteristicName,
                            SelectedAnswer = characteristic.ID.ToString()

                        };
                        q1.Answers.Add(new Answer
                        {
                            ID = characteristic.ID,
                            AnswerText = characteristic.CharacteristcValue
                        });
                    }

                    idCharacteristic = characteristic.Characteristics.ID;
                }
                productContainer.Evaluation = evalVM;
                return View(productContainer);
            }
            catch
            {
                return View(product);
            }
        }

        /// <summary>
        /// Добавление товара в корзину
        /// </summary>
        /// <param name="model">Модель выбранного товара</param>
        /// <param name="quantity">Количество выбранного товара</param>
        /// <returns>Страница товара.</returns>
        [HttpPost]
        public IActionResult AddBasket(Product model, int quantity)
        {
            var response = new ApiRequest().Get($@"product/{model.ID}");
            Product product = JsonConvert.DeserializeObject<Product>(response.Content);
            List<int> idProductCharacteristicsList = new List<int>();
            response = new ApiRequest().Get($@"allCharacteristics/{product.Subcategory.ID}");

            if (!response.Content.Contains("У данной подкатегории нет характеристик"))
            {
                List<Characteristics> characteristicsList = JsonConvert.DeserializeObject<List<Characteristics>>(response.Content);
                foreach (var characteristic in characteristicsList)
                {
                    for (int i = 0; i < product.ProductCharacteristicsList.Count; i++)
                    {
                        if (characteristic.ID == product.ProductCharacteristicsList[i].Characteristics.ID)
                        {
                            product.ProductCharacteristicsList[i].Characteristics = characteristic;
                        }
                    }
                }
            }

            if (model.Evaluation != null)
            {
                foreach (var q in model.Evaluation.Questions)
                {
                    idProductCharacteristicsList.Add(Convert.ToInt32(q.SelectedAnswer));
                }
                idProductCharacteristicsList.Add(0);
            }
            else
            {
                foreach (var q in product.ProductCharacteristicsList)
                {
                    idProductCharacteristicsList.Add(q.ID);
                }
                idProductCharacteristicsList.Add(0);
            }

            Basket newBasket = new Basket
            {
                Product = product,
                Quantity = quantity,
                IDProductCharacteristicsList = idProductCharacteristicsList
            };

            var basket = HttpContext.Session.GetObjectFromJson<List<Basket>>("Basket");
            if(basket != null)
            {
                basket.Add(newBasket);
            }
            else
            {
                basket = new List<Basket>() { newBasket};

            }

            HttpContext.Session.SetObjectAsJson("Basket", basket);

            HttpContext.Session.SetObjectAsJson("BasketCount", HttpContext.Session.GetObjectFromJson<int>("BasketCount")+1);

            ViewBag.Message = "Успешное добавление товара в корзину";
            product.Evaluation = model.Evaluation;
            return RedirectToAction("Index", "SelectedProduct");
        }
    }
}

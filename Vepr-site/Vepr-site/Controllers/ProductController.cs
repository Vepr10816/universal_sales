using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using RestSharp;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Vepr_site.Models;

namespace Vepr_site.Controllers
{
    /// <summary>
    /// Контроллер страницы каталога подкатегории..
    /// </summary>
    public class ProductController : Controller
    {
        /// <summary>
        /// Вывод страницы с товарами.
        /// Заполнение модели для страницы, сортировка данных модели.
        /// </summary>
        /// <returns>Страница с товарами.</returns>
        [HttpGet]
        public IActionResult Index()
        {
            int idSubcategory = HttpContext.Session.GetObjectFromJson<int>("IDSubcategory");
            var response = new ApiRequest().Get($@"allProduct/{idSubcategory}");
            List<Product> productList = JsonConvert.DeserializeObject<List<Product>>(response.Content);
            List<CharacteristicsFilter> characteristicsFilterList = new List<CharacteristicsFilter>();
            try
            {
                response = new ApiRequest().Get($@"allCharacteristics/{idSubcategory}");
                List<Characteristics> characteristicsList = JsonConvert.DeserializeObject<List<Characteristics>>(response.Content);
                foreach (var characteristic in characteristicsList)
                {
                    List<CharacteristicValues> characteristicValuesList = new List<CharacteristicValues>();
                    foreach (var product in productList)
                    {
                        foreach (var characteriticProduct in product.ProductCharacteristicsList.Where(x => x.Characteristics.ID == characteristic.ID))
                        {
                            /*if (characteristicValuesList.Where(x => x.CharacteteristicValue == characteriticProduct.CharacteristcValue).Count() == 0)
                            {
                                characteristicValuesList.Add(
                                    new CharacteristicValues { CharacteteristicValue = characteriticProduct.CharacteristcValue });
                            }*/
                            if (!characteristicValuesList.Where(x => x.CharacteteristicValue == characteriticProduct.CharacteristcValue).Any())
                            {
                                characteristicValuesList.Add(
                                    new CharacteristicValues { CharacteteristicValue = characteriticProduct.CharacteristcValue });
                            }
                        }
                    }
                    CharacteristicsFilter characteristicsFilter = new CharacteristicsFilter
                    {
                        Id = characteristic.ID,
                        CharacteristicName = characteristic.CharacteristicName,
                        CharacteristicValuesList = characteristicValuesList
                    };
                    characteristicsFilterList.Add(characteristicsFilter);
                }
            }
            catch
            {
                characteristicsFilterList = null;
            }
            ProductWithCharacteristics productWithCharacteristicsList = new ProductWithCharacteristics
            {
                CharacteristicsFilterList = characteristicsFilterList,
                ProductList = productList
            };
            ViewBag.SubcategoryName = productList[0].Subcategory.SubcategoryName;
            ViewBag.IDSubcategory = productList[0].Subcategory.ID;
            return View(productWithCharacteristicsList);
        }

        /// <summary>
        /// Фильтрация товаров по значениям.
        /// Заполнение модели сортированными данными.
        /// </summary>
        /// <param name="productWithCharacteristics">Модель товара с характеристиками</param>
        /// <returns>Страница с отфильтрованными товарами.</returns>
        [HttpPost]
        public IActionResult ProductFilter(ProductWithCharacteristics productWithCharacteristics)
        {
            var response = new ApiRequest().Get($@"allProduct/{productWithCharacteristics.ProductList[0].Subcategory.ID}");
            List<Product> productList = JsonConvert.DeserializeObject<List<Product>>(response.Content);
            ViewBag.IDSubcategory = productList[0].Subcategory.ID;
            productWithCharacteristics.ProductList = productList;
            
            if (!productWithCharacteristics.CharacteristicsFilterList.Any(x => x.CharacteristicValuesList.Any(y => y.IsSelected)))
            {
                productWithCharacteristics.ProductList = productList;
                return View("Index", productWithCharacteristics);
            }
            else
            {
                List<Product> productListContainer = new List<Product>();
                List<string> selectedValuesList = new List<string>();
                List<int> characteristicsIDList = new List<int>();
                foreach (CharacteristicsFilter characteristicsFilter in productWithCharacteristics.CharacteristicsFilterList)
                {
                    /*if (characteristicsFilter.CharacteristicValuesList.Count(x => x.IsSelected == true) > 0)
                        characteristicsIDList.Add(characteristicsFilter.Id);*/
                    if (characteristicsFilter.CharacteristicValuesList.Any(x => x.IsSelected == true))
                        characteristicsIDList.Add(characteristicsFilter.Id);
                    foreach (CharacteristicValues characteristicValues in characteristicsFilter.CharacteristicValuesList)
                    {
                        if (characteristicValues.IsSelected)
                        {
                            selectedValuesList.Add(characteristicValues.CharacteteristicValue);
                        }
                    }
                }

                foreach (var product in productWithCharacteristics.ProductList)
                {
                    foreach(var productCharacteristics in product.ProductCharacteristicsList)
                    {
                        if(
                            characteristicsIDList.Contains(productCharacteristics.Characteristics.ID) &&
                            selectedValuesList.Contains(productCharacteristics.CharacteristcValue)
                            )
                        {
                            productListContainer.Add(product);
                        }
                    }
                }

                HashSet<Product> uniqueValuesProductList = new HashSet<Product>(productListContainer);
                List<Product> sortedProductList = new List<Product>(uniqueValuesProductList);
                int i = 0;
                foreach (var element in productListContainer)
                {
                    if (!uniqueValuesProductList.Contains(element))
                    {
                        sortedProductList.Insert(i, element);
                        i++;
                    }
                }
                productWithCharacteristics.ProductList = sortedProductList;
                return View("Index",productWithCharacteristics);

            }
        }

        /// <summary>
        /// Перенправление на страницу с выбранным товаром.
        /// </summary>
        /// <param name="idProduct">первичный ключ товара.</param>
        /// <returns>Страница выбранного товара.</returns>
        [HttpGet]
        public ActionResult RedirectToSelectedProduct(int idProduct)
        {
            HttpContext.Session.SetObjectAsJson("IDProduct", idProduct);
            return RedirectToAction("Index", "SelectedProduct");
        }
    }
}

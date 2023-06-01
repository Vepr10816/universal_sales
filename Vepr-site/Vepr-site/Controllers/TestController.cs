
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using RestSharp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Vepr_site.Models;

namespace Vepr_site.Controllers
{
    public class TestController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Index(Person model)
        {
            if (ModelState.IsValid)
            {
                // Сохраняем данные модели в сессии
                //HttpContext.Session.SetObjectAsJson("Person", model);

                return RedirectToAction("Index1");
            }

            // Если данные модели не верные, возвращаем форму с сообщением об ошибке
            return View(model);
        }

        public IActionResult Index1()
        {
            var person = HttpContext.Session.GetObjectFromJson<Person>("Person");

            return View(person);
        }

        /*public ActionResult Index()
        {
            var client = new RestClient("http://127.0.0.1:8081");
            var request = new RestRequest($@"product/52");
            var response = client.Get(request);
            Product product = JsonConvert.DeserializeObject<Product>(response.Content);

            Product productContainer = JsonConvert.DeserializeObject<Product>(response.Content);
            request = new RestRequest($@"allCharacteristics/{product.subcategory.id}");
            response = client.Get(request);
            List<Characteristics> characteristicsList = JsonConvert.DeserializeObject<List<Characteristics>>(response.Content);
            foreach (var characteristic in characteristicsList)
            {
                for (int i = 0; i < product.productCharacteristicsList.Count; i++)
                {
                    if (characteristic.id == product.productCharacteristicsList[i].characteristics.id)
                    {
                        productContainer.productCharacteristicsList[i].characteristics = characteristic;
                    }
                }
            }
            var evalVM = new Evaluation();
            int idCharacteristic = 0;
            var q1 = new Question();
            var productCharacteristicsList = productContainer.productCharacteristicsList
                .Where(x => x.characteristics.selectable &&
                    productContainer.productCharacteristicsList.Count(y => y.characteristics.id == x.characteristics.id) > 1)
                .ToList();
            for (int i = 0; i < productCharacteristicsList.Count; i++)
            {
                var characteristic = productCharacteristicsList[i];

                if (characteristic.characteristics.id == idCharacteristic)
                {
                    q1.Answers.Add(new Answer
                    {
                        ID = characteristic.id,
                        AnswerText = characteristic.characteristc_value
                    });

                    if (i == productCharacteristicsList.Count - 1 ||
                        characteristic.characteristics.id != productContainer.productCharacteristicsList[i + 1].characteristics.id)
                    {
                        evalVM.Questions.Add(q1);
                    }
                }
                else
                {
                    q1 = new Question
                    {
                        ID = characteristic.characteristics.id,
                        QuestionText = characteristic.characteristics.characteristic_name
                    };
                    q1.Answers.Add(new Answer
                    {
                        ID = characteristic.id,
                        AnswerText = characteristic.characteristc_value
                    });
                }

                idCharacteristic = characteristic.characteristics.id;
            }

            return View(evalVM);
        }*/

        /*[HttpPost]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        public string Index(Evaluation model, string b)
        {
            *//*if (ModelState.IsValid)
            {*//*
            string a = "";
                foreach (var q in model.Questions)
                {
                    var qId = q.ID;
                    var selectedAnswer = q.SelectedAnswer;
                a += selectedAnswer + " ";

                }
                return "You choose - " + a + " //////"+b; //PRG Pattern
            *//*}
            //to do : reload questions and answers
            return View(model);*//*
        }*/
        /*[HttpGet]
        public ActionResult Index()
        {
            var client = new RestClient("http://127.0.0.1:8081");
            var request = new RestRequest("allCategoryFromUser/1");
            var response = client.Get(request);
            List<Category> categoryList = JsonConvert.DeserializeObject<List<Category>>(response.Content);
            categoryList.RemoveAll(category => category.subcategoryList.Count == 0);
            return View(categoryList);
        }

        [HttpPost]
        public string Index(List<string> color)
        {
            string a = "";
            foreach (string item in color)
            {
                a += item + " ";
            }
            return $@"you choose - {a}";
        }*/

        /*[HttpPost]
        public string Index(IEnumerable<Category> categories)
        {
            if (categories.Count(x => x.isSelected) == 0)
            {
                return "You have not selected any Category";
            }
            else
            {
                StringBuilder sb = new StringBuilder();
                sb.Append("You selected - ");
                foreach (Category category in categories)
                {
                    if (category.isSelected)
                    {
                        sb.Append(category.category_name + ", ");
                    }
                }
                sb.Remove(sb.ToString().LastIndexOf(","), 1);
                return sb.ToString();
            }
        }*/
    }
}

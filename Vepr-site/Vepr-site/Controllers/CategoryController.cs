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
    public class CategoryController : Controller
    {
        public IActionResult Index()
        {
            var response = new ApiRequest().Get("allCategoryFromUser/1");
            List<Category> categoryList = JsonConvert.DeserializeObject<List<Category>>(response.Content);
            categoryList.RemoveAll(category => category.SubcategoryList.Count == 0);
            return View(categoryList);
        }

        [HttpPost]
        public ActionResult RedirectToSubcategory(int idCategory)
        {
            HttpContext.Session.SetObjectAsJson("IDCategory", idCategory);
            return RedirectToAction("Index", "Subcategory");
        }
    }
}

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
    public class SubcategoryController : Controller
    {
        [HttpGet]
        public IActionResult Index()
        {
            int idCategory = HttpContext.Session.GetObjectFromJson<int>("IDCategory");
            var response = new ApiRequest().Get($@"allSubcategory/{idCategory}");
            List<Subcategory> subcategoryList = JsonConvert.DeserializeObject<List<Subcategory>>(response.Content);
            subcategoryList.RemoveAll(subcategory => subcategory.ProductList.Count == 0);
            ViewBag.CategoryName = subcategoryList[0].Category.CategoryName;
            return View(subcategoryList);
        }

        [HttpGet]
        public ActionResult RedirectToProduct(int idSubcategory)
        {
            HttpContext.Session.SetObjectAsJson("IDSubcategory", idSubcategory);
            return RedirectToAction("Index", "Product");
        }
    }
}

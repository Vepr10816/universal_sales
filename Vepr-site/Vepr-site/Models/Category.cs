using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site.Models
{
    public class Category
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "category_name")]
        public string CategoryName { get; set; }

        [JsonProperty(PropertyName = "mycompany")]
        public MyCompany MyCompany { get; set; }

        [JsonProperty(PropertyName = "subcategoryList")]
        public List<Subcategory> SubcategoryList { get; set; }
        public bool IsSelected { get; set; } = false;
    }
}

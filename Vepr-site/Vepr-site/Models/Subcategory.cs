using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site.Models
{
    public class Subcategory
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "subcategory_name")]
        public string SubcategoryName { get; set; }

        [JsonProperty(PropertyName = "category")]
        public Category Category { get; set; }

        [JsonProperty(PropertyName = "productList")]
        public List<Product> ProductList { get; set; }
    }
}

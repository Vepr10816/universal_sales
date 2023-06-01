using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site.Models
{
    public class ProductWithCharacteristics
    {
        [JsonProperty(PropertyName = "productList")]
        public List<Product> ProductList { get; set; }

        [JsonProperty(PropertyName = "characteristicsFilterList")]
        public List<CharacteristicsFilter> CharacteristicsFilterList { get; set; }
    }
}

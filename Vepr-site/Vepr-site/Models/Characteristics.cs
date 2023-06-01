using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site.Models
{
    public class Characteristics
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "characteristic_name")]
        public string CharacteristicName { get; set; }

        [JsonProperty(PropertyName = "selectable")]
        public bool Selectable { get; set; }

        [JsonProperty(PropertyName = "subcategory")]
        public Subcategory Subcategory { get; set; }

        [JsonProperty(PropertyName = "datatype")]
        public Datatype Datatype { get; set; }

        [JsonProperty(PropertyName = "preValuesList")]
        public List<PreValues> PreValuesList { get; set; }
    }


        public class PreValues
        {
            [JsonProperty(PropertyName = "id")]
            public int ID { get; set; }

            [JsonProperty(PropertyName = "pre_value")]
            public string PreValue { get; set; }

            [JsonProperty(PropertyName = "characteristics")]
            public Characteristics Characteristics { get; set; }
        }

        public class Datatype
        {
            [JsonProperty(PropertyName = "id")]
            public int ID { get; set; }

            [JsonProperty(PropertyName = "type_name")]
            public string TypeName { get; set; }
        }
}

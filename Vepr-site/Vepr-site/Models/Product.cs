using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site.Models
{

    public class Product
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "product_name")]
        public string ProductName { get; set; }

        [JsonProperty(PropertyName = "description")]
        public string Description { get; set; }

        [JsonProperty(PropertyName = "product_price")]
        public double ProductPrice { get; set; }

        [JsonProperty(PropertyName = "subcategory")]
        public Subcategory Subcategory { get; set; }

        [JsonProperty(PropertyName = "productPhotosList")]
        public List<ProductPhotos> ProductPhotosList { get; set; }

        [JsonProperty(PropertyName = "productCharacteristicsList")]
        public List<ProductCharacteristics> ProductCharacteristicsList { get; set; }

        [JsonProperty(PropertyName = "currency")]
        public Currency Currency { get; set; }

        public Evaluation Evaluation { get; set; }
    }

    public class Currency
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "currency_name")]
        public string CurrencyName { get; set; }
    }

    public class ProductCharacteristics
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "characteristc_value")]
        public string CharacteristcValue { get; set; }

        [JsonProperty(PropertyName = "product")]
        public Product Product { get; set; }

        [JsonProperty(PropertyName = "characteristics")]
        public Characteristics Characteristics { get; set; }
    }

    public class ProductPhotos
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "url_photo")]
        public string UrlPhoto { get; set; }

        [JsonProperty(PropertyName = "photo_name")]
        public string PhotoName { get; set; }

        [JsonProperty(PropertyName = "product")]
        public Product Product { get; set; }
    }

}

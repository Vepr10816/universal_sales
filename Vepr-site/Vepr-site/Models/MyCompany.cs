using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site.Models
{
    public class MyCompany
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "company_name")]
        public string CompanyName { get; set; }

        [JsonProperty(PropertyName = "description")]
        public string Description { get; set; }

        [JsonProperty(PropertyName = "url_logo")]
        public string UrlLogo { get; set; }
    }

    public class Requisites
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "requisites_name")]
        public string RequisitesName { get; set; }

        [JsonProperty(PropertyName = "requisites_value")]
        public string RequisitesValue { get; set; }

        [JsonProperty(PropertyName = "mycompany")]
        public MyCompany MyCompany { get; set; }
    }

    public class Address
    {
        [JsonProperty(PropertyName = "id")]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "address_name")]
        public string AddressName { get; set; }

        [JsonProperty(PropertyName = "mycompany")]
        public MyCompany MyCompany { get; set; }
    }

    public class Company
    {
        public MyCompany MyCompany { get; set; }
        public List<Address> Addresses { get; set; }
        public List<Requisites> Requisites { get; set; }

    }
}

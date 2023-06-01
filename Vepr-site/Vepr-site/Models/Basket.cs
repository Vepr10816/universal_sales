using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site.Models
{
    public class Basket
    {
        public Product Product { get; set; }
        public int Quantity { get; set; }
        public double Price => Product.ProductPrice * Quantity;
        public List<int> IDProductCharacteristicsList { get; set; }
    }
}

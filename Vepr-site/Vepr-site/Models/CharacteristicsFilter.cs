using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Vepr_site.Models
{
    public class CharacteristicsFilter
    {
        public int Id { get; set; }
        public string CharacteristicName { get; set; }
        public List<CharacteristicValues> CharacteristicValuesList { get; set; }
    }

    public class CharacteristicValues
    {
        public string CharacteteristicValue { get; set; }
        public bool IsSelected { get; set; } = false;
    }
}

#pragma checksum "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "3c136235f8d11b9d44ca16e3895f264934e05f21"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_SelectedProduct_Index1), @"mvc.1.0.view", @"/Views/SelectedProduct/Index1.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\_ViewImports.cshtml"
using Vepr_site;

#line default
#line hidden
#nullable disable
#nullable restore
#line 1 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
using Vepr_site.Models;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
using System;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
using System.IO;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"3c136235f8d11b9d44ca16e3895f264934e05f21", @"/Views/SelectedProduct/Index1.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"e0dac435382d58e05d7c21b21f2bf41af03211d5", @"/Views/_ViewImports.cshtml")]
    public class Views_SelectedProduct_Index1 : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<Product>
    {
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
#nullable restore
#line 5 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
  
    ViewData["Title"] = Model.ProductName;

#line default
#line hidden
#nullable disable
            WriteLiteral("    <h1>");
#nullable restore
#line 7 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
   Write(ViewData["Title"]);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h1>\r\n");
            WriteLiteral("\r\n");
            WriteLiteral("    <h3>");
#nullable restore
#line 11 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
   Write(Model.Description);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h3>\r\n    <h4>");
#nullable restore
#line 12 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
   Write(Model.ProductPrice);

#line default
#line hidden
#nullable disable
            WriteLiteral(" руб</h4>\r\n");
#nullable restore
#line 13 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
    foreach (var photo in Model.ProductPhotosList)
    {
        string pathPhoto = $@"{System.IO.Path.DirectorySeparatorChar}images{System.IO.Path.DirectorySeparatorChar}{photo.PhotoName}";

#line default
#line hidden
#nullable disable
            WriteLiteral("        <img");
            BeginWriteAttribute("src", " src=\"", 443, "\"", 472, 1);
#nullable restore
#line 16 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
WriteAttributeValue("", 449, Url.Content(pathPhoto), 449, 23, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            WriteLiteral(" alt=\"Image\" />\r\n");
#nullable restore
#line 17 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
    }

    string characteristicName = "";
    string strForCharacteristicProduct = "";
    if (Model.ProductCharacteristicsList.Count != 0)
    {
        foreach (var characteristic in Model.ProductCharacteristicsList)
        {
            if (characteristic.Characteristics.Selectable == true && Model.ProductCharacteristicsList.Count(x => x.Characteristics.ID == characteristic.Characteristics.ID) > 1)
            {
                

#line default
#line hidden
#nullable disable
#nullable restore
#line 35 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
                       
                if (characteristicName == characteristic.Characteristics.CharacteristicName)
                {

#line default
#line hidden
#nullable disable
            WriteLiteral("                    <p>");
#nullable restore
#line 38 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
                  Write(characteristic.CharacteristcValue);

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\r\n");
#nullable restore
#line 39 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
                }
                else
                {

#line default
#line hidden
#nullable disable
            WriteLiteral("                    <h5>");
#nullable restore
#line 42 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
                   Write(characteristic.Characteristics.CharacteristicName);

#line default
#line hidden
#nullable disable
            WriteLiteral(":</h5>\r\n                    <p>");
#nullable restore
#line 43 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
                  Write(characteristic.CharacteristcValue);

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\r\n");
#nullable restore
#line 44 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
                }

#line default
#line hidden
#nullable disable
            WriteLiteral("                <p>");
#nullable restore
#line 45 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
              Write(strForCharacteristicProduct);

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\r\n");
#nullable restore
#line 46 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"

                characteristicName = characteristic.Characteristics.CharacteristicName;
            }
        }


#line default
#line hidden
#nullable disable
            WriteLiteral("        <h4>Характеристики:</h4>\r\n");
#nullable restore
#line 52 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
        characteristicName = "";
        strForCharacteristicProduct = "";
        foreach (var characteristic in Model.ProductCharacteristicsList)
        {
            if (characteristic.Characteristics.Selectable == false ||
                (characteristic.Characteristics.Selectable == true &&
                Model.ProductCharacteristicsList.Count(x => x.Characteristics.ID == characteristic.Characteristics.ID) == 1))
                if (characteristicName == characteristic.Characteristics.CharacteristicName)
                {
                    strForCharacteristicProduct = $@", {characteristic.CharacteristcValue}";
                }
                else
                {
                    strForCharacteristicProduct = $@"{characteristic.Characteristics.CharacteristicName} - {characteristic.CharacteristcValue}";
                }

#line default
#line hidden
#nullable disable
            WriteLiteral("            <p>");
#nullable restore
#line 67 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
          Write(strForCharacteristicProduct);

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\r\n");
#nullable restore
#line 68 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index1.cshtml"
            characteristicName = characteristic.Characteristics.CharacteristicName;
        }
    }
    

#line default
#line hidden
#nullable disable
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<Product> Html { get; private set; }
    }
}
#pragma warning restore 1591

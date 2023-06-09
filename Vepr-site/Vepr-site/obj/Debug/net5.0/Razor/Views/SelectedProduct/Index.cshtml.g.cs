#pragma checksum "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "ab48ae83f8caaba1c44e8aa1da2b365de9b80a43"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_SelectedProduct_Index), @"mvc.1.0.view", @"/Views/SelectedProduct/Index.cshtml")]
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
#line 1 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
using Vepr_site.Models;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
using System;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
using System.IO;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"ab48ae83f8caaba1c44e8aa1da2b365de9b80a43", @"/Views/SelectedProduct/Index.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"e0dac435382d58e05d7c21b21f2bf41af03211d5", @"/Views/_ViewImports.cshtml")]
    public class Views_SelectedProduct_Index : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<Product>
    {
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
#nullable restore
#line 5 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
  
    ViewData["Title"] = Model.ProductName;
    string characteristicName = "";
    string strForCharacteristicProduct = "";

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n");
#nullable restore
#line 11 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
  
    List<string> characteristicsList = new List<string>();
    foreach (var characteristic in Model.ProductCharacteristicsList)
    {
        if (characteristic.Characteristics.Selectable == false ||
            (characteristic.Characteristics.Selectable == true &&
            Model.ProductCharacteristicsList.Count(x => x.Characteristics.ID == characteristic.Characteristics.ID) == 1))
        {
            if (characteristicName == characteristic.Characteristics.CharacteristicName)
            {
                characteristicsList[characteristicsList.Count] += $@", {characteristic.CharacteristcValue}";
            }
            else
            {
                characteristicsList.Add($@"{characteristic.Characteristics.CharacteristicName} - {characteristic.CharacteristcValue}");
            }
            

#line default
#line hidden
#nullable disable
#nullable restore
#line 27 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                                                   
            characteristicName = characteristic.Characteristics.CharacteristicName;
        }
    }

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n<div class=\"col d-flex flex-column\">\r\n    <h1 class=\"text-center\">");
#nullable restore
#line 34 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                       Write(Model.ProductName);

#line default
#line hidden
#nullable disable
            WriteLiteral(@"</h1>
    <div class=""row"">
        <div class=""container"">
            <div id=""myCarousel"" class=""carousel slide"" data-ride=""carousel"" data-interval=""2000"" data-pause=""hover"">
                <!-- Indicators -->
                <ol class=""carousel-indicators"">
");
#nullable restore
#line 40 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                     for (int i = 0; i < Model.ProductPhotosList.Count; i++)
                    {
                        if (i == 0)
                        {

#line default
#line hidden
#nullable disable
            WriteLiteral("                            <li data-target=\"#myCarousel\" data-slide-to=\"");
#nullable restore
#line 44 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                                                                    Write(i);

#line default
#line hidden
#nullable disable
            WriteLiteral("\" class=\"active\"></li>\r\n");
#nullable restore
#line 45 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                        }
                        else
                        {

#line default
#line hidden
#nullable disable
            WriteLiteral("                            <li data-target=\"#myCarousel\" data-slide-to=\"");
#nullable restore
#line 48 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                                                                    Write(i);

#line default
#line hidden
#nullable disable
            WriteLiteral("\"></li>\r\n");
#nullable restore
#line 49 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                        }
                    }

#line default
#line hidden
#nullable disable
            WriteLiteral("                </ol>\r\n                <!-- Wrapper for slides -->\r\n                <div class=\"carousel-inner\" role=\"listbox\">\r\n");
#nullable restore
#line 54 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                     for (int i = 0; i < Model.ProductPhotosList.Count; i++)
                    {
                        if (i == 0)
                        {

#line default
#line hidden
#nullable disable
            WriteLiteral("                            <div class=\"item active\">\r\n                                <div class=\"carousel-content\">\r\n                                    <div style=\"margin: 0 auto\">\r\n                                        <p>\r\n");
#nullable restore
#line 62 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                                              string pathPhoto = $@"{System.IO.Path.DirectorySeparatorChar}images{System.IO.Path.DirectorySeparatorChar}{Model.ProductPhotosList[i].PhotoName}";

#line default
#line hidden
#nullable disable
            WriteLiteral("                                            <img alt=\"img\"");
            BeginWriteAttribute("src", " src=\"", 2809, "\"", 2838, 1);
#nullable restore
#line 63 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
WriteAttributeValue("", 2815, Url.Content(pathPhoto), 2815, 23, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            WriteLiteral("\r\n                                                 style=\"width: 100%;height: 200px\" />\r\n                                        </p>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n");
#nullable restore
#line 69 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                        }
                        else
                        {

#line default
#line hidden
#nullable disable
            WriteLiteral("                            <div class=\"item\">\r\n                                <div class=\"carousel-content\">\r\n                                    <div style=\"margin: 0 auto;text-align:center;\">\r\n                                        <p>\r\n");
#nullable restore
#line 76 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                                              string pathPhoto = $@"{System.IO.Path.DirectorySeparatorChar}images{System.IO.Path.DirectorySeparatorChar}{Model.ProductPhotosList[i].PhotoName}";

#line default
#line hidden
#nullable disable
            WriteLiteral("                                            <img alt=\"img\"");
            BeginWriteAttribute("src", " src=\"", 3673, "\"", 3702, 1);
#nullable restore
#line 77 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
WriteAttributeValue("", 3679, Url.Content(pathPhoto), 3679, 23, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            WriteLiteral("\r\n                                                 style=\"width: 100%;height: 200px\" />\r\n                                        </p>\r\n                                    </div>\r\n                                </div>\r\n                            </div>\r\n");
#nullable restore
#line 83 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                        }
                    }

#line default
#line hidden
#nullable disable
            WriteLiteral(@"                </div>
                <a class=""left carousel-control"" href=""#myCarousel"" role=""button"" data-slide=""prev"">
                    <span class=""glyphicon glyphicon-chevron-left"" aria-hidden=""true""></span>
                    <span class=""sr-only""> Previous</span>
                </a>
                <a class=""right carousel-control"" href=""#myCarousel"" role=""button"" data-slide=""next"">
                    <span class=""glyphicon glyphicon-chevron-right"" aria-hidden=""true""></span>
                    <span class=""sr-only"">Next</span>
                </a>
            </div>
            <link rel=""stylesheet"" href=""https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"" />
            <link rel=""stylesheet"" href=""https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"" />
            <script type=""text/javascript"" src=""https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js""></script>
            <script type=""text/javascript"" src=""https://maxcdn");
            WriteLiteral(@".bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js""></script>
            <style type=""text/css"">
                .carousel-inner {
                    width: auto;
                    height: 200px;
                    max-height: 200px !important;
                }

                .carousel-content {
                    color: black;
                    display: flex;
                    text-align: center;
                }
            </style>
            <script type=""text/javascript"">
                $(document).ready(function () {
                    $('.carousel').carousel();
                });
            </script>
        </div>
    </div>
    <div class=""row mt-2"">
        <div class=""col-6"">
            <p>");
#nullable restore
#line 121 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
          Write(Model.Description);

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\r\n        </div>\r\n        <div class=\"col-6\">\r\n            <p>");
#nullable restore
#line 124 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
          Write(Model.ProductPrice);

#line default
#line hidden
#nullable disable
            WriteLiteral(" руб</p>\r\n        </div>\r\n    </div>\r\n");
#nullable restore
#line 127 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
     using (Html.BeginForm("AddBasket", "SelectedProduct", FormMethod.Post))
    {
        

#line default
#line hidden
#nullable disable
            WriteLiteral(@"        <div class=""row mt-1"">
            <div class=""col-6"">
                <p>Характеристики</p>
            </div>
            <div class=""col-6"">
                <p><input type=""number"" name=""quantity"" value=""1"" max=""10"" min=""1"" step=""1""> шт.</p>
            </div>
        </div>
");
            WriteLiteral("        <div class=\"row mt-1\">\r\n            <div class=\"col-6\">\r\n                ");
#nullable restore
#line 143 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
           Write(Html.HiddenFor(item => item.ID));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n                ");
#nullable restore
#line 144 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
           Write(Html.EditorFor(x => x.Evaluation.Questions));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </div>\r\n            <div class=\"col-6\">\r\n                <input class=\"btn btn-primary\" type=\"submit\" value=\"Добавить в корзину\" />\r\n            </div>\r\n        </div>\r\n");
#nullable restore
#line 150 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
    }

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n");
#nullable restore
#line 152 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
     if (Model.ProductCharacteristicsList.Count != 0)
    {

#line default
#line hidden
#nullable disable
            WriteLiteral("        <h3 class=\"text-center\">Характеристики</h3>\r\n");
            WriteLiteral("        <div class=\"row mt-1\">\r\n");
#nullable restore
#line 157 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
             foreach (var characteristic in characteristicsList)
            {

#line default
#line hidden
#nullable disable
            WriteLiteral("                <div class=\"col-6\">\r\n                    <p>");
#nullable restore
#line 160 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
                  Write(characteristic);

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\r\n                </div>\r\n");
#nullable restore
#line 162 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
            }

#line default
#line hidden
#nullable disable
            WriteLiteral("        </div>\r\n");
#nullable restore
#line 164 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\SelectedProduct\Index.cshtml"
    }

#line default
#line hidden
#nullable disable
            WriteLiteral("</div>\r\n\r\n");
            WriteLiteral("\r\n");
            WriteLiteral("\r\n");
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

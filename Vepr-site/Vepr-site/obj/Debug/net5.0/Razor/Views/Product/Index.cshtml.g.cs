#pragma checksum "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "c87a319deeb8a004ffc041157f8f8d1b37f50f80"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Product_Index), @"mvc.1.0.view", @"/Views/Product/Index.cshtml")]
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
#line 1 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
using Vepr_site.Models;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
using System;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
using System.IO;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"c87a319deeb8a004ffc041157f8f8d1b37f50f80", @"/Views/Product/Index.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"e0dac435382d58e05d7c21b21f2bf41af03211d5", @"/Views/_ViewImports.cshtml")]
    public class Views_Product_Index : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<ProductWithCharacteristics>
    {
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_0 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("name", new global::Microsoft.AspNetCore.Html.HtmlString("Product"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_1 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("class", new global::Microsoft.AspNetCore.Html.HtmlString("btn btn-primary"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_2 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("asp-action", "RedirectToSelectedProduct", global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_3 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("asp-controller", "Product", global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        #line hidden
        #pragma warning disable 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperExecutionContext __tagHelperExecutionContext;
        #pragma warning restore 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner __tagHelperRunner = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner();
        #pragma warning disable 0169
        private string __tagHelperStringValueBuffer;
        #pragma warning restore 0169
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __backed__tagHelperScopeManager = null;
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __tagHelperScopeManager
        {
            get
            {
                if (__backed__tagHelperScopeManager == null)
                {
                    __backed__tagHelperScopeManager = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager(StartTagHelperWritingScope, EndTagHelperWritingScope);
                }
                return __backed__tagHelperScopeManager;
            }
        }
        private global::Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper;
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
#nullable restore
#line 5 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
  
    ViewData["Title"] = ViewBag.SubcategoryName;
    int sb = ViewBag.IDSubcategory;
    Product pr = new Product { Subcategory = new Subcategory { ID = sb } };
    Model.ProductList.Add(pr);

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n");
            WriteLiteral("\r\n<div class=\"col d-flex flex-column\">\r\n    <h1 class=\"text-center\">");
#nullable restore
#line 68 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                       Write(ViewData["Title"]);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h1>\r\n    <div class=\"row mt-2\">\r\n");
#nullable restore
#line 70 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
         if (Model.CharacteristicsFilterList != null)
        {
            

#line default
#line hidden
#nullable disable
#nullable restore
#line 72 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
             using (Html.BeginForm("ProductFilter", "Product", FormMethod.Post, new { @class = "col-6" }))
            {

                for (int i = 0; i < Model.ProductList.Count(); i++)
                {
                    

#line default
#line hidden
#nullable disable
#nullable restore
#line 77 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
               Write(Html.HiddenFor(item => item.ProductList[i].Subcategory.ID));

#line default
#line hidden
#nullable disable
#nullable restore
#line 77 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                                                                               
                }

#line default
#line hidden
#nullable disable
            WriteLiteral("                <div>\r\n\r\n");
#nullable restore
#line 81 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                     for (var i = 0; i < Model.CharacteristicsFilterList.Count(); i++)
                    {

#line default
#line hidden
#nullable disable
            WriteLiteral("                        <p class=\"font-weight-bold mt-2 text-center\">");
#nullable restore
#line 83 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                                                                Write(Model.CharacteristicsFilterList[i].CharacteristicName);

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\r\n");
#nullable restore
#line 84 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                        for (var j = 0; j < Model.CharacteristicsFilterList[i].CharacteristicValuesList.Count(); j++)
                        {
                            

#line default
#line hidden
#nullable disable
#nullable restore
#line 86 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                       Write(Html.HiddenFor(item => item.CharacteristicsFilterList[i].Id));

#line default
#line hidden
#nullable disable
#nullable restore
#line 87 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                       Write(Html.HiddenFor(item => item.CharacteristicsFilterList[i].CharacteristicName));

#line default
#line hidden
#nullable disable
#nullable restore
#line 88 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                       Write(Html.HiddenFor(item => item.CharacteristicsFilterList[i].CharacteristicValuesList[j].CharacteteristicValue));

#line default
#line hidden
#nullable disable
            WriteLiteral(@"                            <div class=""row"" style=""display: flex; align-items: center; justify-content: center;"">
                                <div class=""col-3"" style=""display: flex; align-items: end; justify-content: end;"">
                                    ");
#nullable restore
#line 91 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                               Write(Html.CheckBoxFor(item => item.CharacteristicsFilterList[i].CharacteristicValuesList[j].IsSelected, new { Style = "hori-align:3px}" }));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n                                </div>\r\n                                <div class=\"col-3\" style=\"display: flex; align-items: start; justify-content: start;\">\r\n                                    ");
#nullable restore
#line 94 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                               Write(Html.DisplayFor(item => item.CharacteristicsFilterList[i].CharacteristicValuesList[j].CharacteteristicValue));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n                                </div>\r\n                            </div>\r\n");
#nullable restore
#line 97 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                        }
                    }

#line default
#line hidden
#nullable disable
            WriteLiteral(@"
                    <div class=""row"" style=""display: flex; align-items: center; justify-content: center;"">
                        <input class=""btn btn-primary mt-2"" id=""Submit1"" type=""submit"" value=""Поиск"" />
                    </div>

                </div>
");
#nullable restore
#line 105 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
            }

#line default
#line hidden
#nullable disable
#nullable restore
#line 105 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
             
        }

#line default
#line hidden
#nullable disable
            WriteLiteral("        <div class=\"col-6\">\r\n");
#nullable restore
#line 108 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                 foreach (var product in Model.ProductList)
                {
                    if (product.ProductPrice > 0)
                    {

#line default
#line hidden
#nullable disable
            WriteLiteral("                        <div class=\"card mb-2\" style=\"width: 18rem;\">\r\n");
#nullable restore
#line 113 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                             if (product.ProductPhotosList.Count > 0)
                            {
                                string pathPhoto = $@"{System.IO.Path.DirectorySeparatorChar}images{System.IO.Path.DirectorySeparatorChar}{product.ProductPhotosList[0].PhotoName}";

#line default
#line hidden
#nullable disable
            WriteLiteral("                                <img");
            BeginWriteAttribute("src", " src=\"", 5602, "\"", 5631, 1);
#nullable restore
#line 116 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
WriteAttributeValue("", 5608, Url.Content(pathPhoto), 5608, 23, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            WriteLiteral(" class=\"card-img-top\" alt=\"image\">\r\n");
#nullable restore
#line 117 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                            }

#line default
#line hidden
#nullable disable
            WriteLiteral("                            <div class=\"card-body\">\r\n                                <h5 class=\"card-title\">");
#nullable restore
#line 119 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                                                  Write(product.ProductName);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h5>\r\n                                <p class=\"card-text\">");
#nullable restore
#line 120 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                                                Write(product.Description);

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\r\n                                ");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("a", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagAndEndTag, "c87a319deeb8a004ffc041157f8f8d1b37f50f8013583", async() => {
                WriteLiteral("Подробнее");
            }
            );
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_0);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_1);
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.Action = (string)__tagHelperAttribute_2.Value;
            __tagHelperExecutionContext.AddTagHelperAttribute(__tagHelperAttribute_2);
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.Controller = (string)__tagHelperAttribute_3.Value;
            __tagHelperExecutionContext.AddTagHelperAttribute(__tagHelperAttribute_3);
            if (__Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.RouteValues == null)
            {
                throw new InvalidOperationException(InvalidTagHelperIndexerAssignment("asp-route-idProduct", "Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper", "RouteValues"));
            }
            BeginWriteTagHelperAttribute();
#nullable restore
#line 121 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                                                                                                                                                   WriteLiteral(product.ID);

#line default
#line hidden
#nullable disable
            __tagHelperStringValueBuffer = EndWriteTagHelperAttribute();
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.RouteValues["idProduct"] = __tagHelperStringValueBuffer;
            __tagHelperExecutionContext.AddTagHelperAttribute("asp-route-idProduct", __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.RouteValues["idProduct"], global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\r\n                            </div>\r\n                        </div>\r\n");
#nullable restore
#line 124 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Product\Index.cshtml"
                    }
                }

#line default
#line hidden
#nullable disable
            WriteLiteral("        </div>\r\n    </div>\r\n</div>\r\n");
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
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<ProductWithCharacteristics> Html { get; private set; }
    }
}
#pragma warning restore 1591

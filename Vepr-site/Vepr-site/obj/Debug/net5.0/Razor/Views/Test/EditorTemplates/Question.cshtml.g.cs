#pragma checksum "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Test\EditorTemplates\Question.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "038318c4430c81aab542623e374e503c534be01c"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Test_EditorTemplates_Question), @"mvc.1.0.view", @"/Views/Test/EditorTemplates/Question.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System;
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
#line 2 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\_ViewImports.cshtml"
using Vepr_site.Models;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"038318c4430c81aab542623e374e503c534be01c", @"/Views/Test/EditorTemplates/Question.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"e0dac435382d58e05d7c21b21f2bf41af03211d5", @"/Views/_ViewImports.cshtml")]
    public class Views_Test_EditorTemplates_Question : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<Vepr_site.Models.Question>
    {
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
            WriteLiteral("<div>\r\n    ");
#nullable restore
#line 3 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Test\EditorTemplates\Question.cshtml"
Write(Html.HiddenFor(x => x.ID));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n    <h3> ");
#nullable restore
#line 4 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Test\EditorTemplates\Question.cshtml"
    Write(Model.QuestionText);

#line default
#line hidden
#nullable disable
            WriteLiteral(" </h3>\r\n");
#nullable restore
#line 5 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Test\EditorTemplates\Question.cshtml"
     foreach (var a in Model.Answers)
    {

#line default
#line hidden
#nullable disable
            WriteLiteral("        <p>\r\n            ");
#nullable restore
#line 8 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Test\EditorTemplates\Question.cshtml"
       Write(Html.RadioButtonFor(b => b.SelectedAnswer, a.ID));

#line default
#line hidden
#nullable disable
            WriteLiteral("  ");
#nullable restore
#line 8 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Test\EditorTemplates\Question.cshtml"
                                                          Write(a.AnswerText);

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n        </p>\r\n");
#nullable restore
#line 10 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Views\Test\EditorTemplates\Question.cshtml"
    }

#line default
#line hidden
#nullable disable
            WriteLiteral("</div>\r\n\r\n");
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
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<Vepr_site.Models.Question> Html { get; private set; }
    }
}
#pragma warning restore 1591

#pragma checksum "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "96c40ad9078e7a56546dae0c6e69868074ccf957"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Cackle_Identity_Telegram_UI_Areas_Identity_Pages_Account_TelegramLoginWidget), @"mvc.1.0.view", @"/Cackle.Identity.Telegram.UI/Areas/Identity/Pages/Account/TelegramLoginWidget.cshtml")]
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
#line 1 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
using Cackle.Identity.Telegram.UI;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"96c40ad9078e7a56546dae0c6e69868074ccf957", @"/Cackle.Identity.Telegram.UI/Areas/Identity/Pages/Account/TelegramLoginWidget.cshtml")]
    public class Cackle_Identity_Telegram_UI_Areas_Identity_Pages_Account_TelegramLoginWidget : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<Cackle.Identity.Telegram.UI.Areas.Identity.Pages.Account.TelegramLoginWidgetModel>
    {
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_0 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("method", "post", global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_1 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("id", new global::Microsoft.AspNetCore.Html.HtmlString("telegramLogin"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
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
        private global::Microsoft.AspNetCore.Mvc.TagHelpers.FormTagHelper __Microsoft_AspNetCore_Mvc_TagHelpers_FormTagHelper;
        private global::Microsoft.AspNetCore.Mvc.TagHelpers.RenderAtEndOfFormTagHelper __Microsoft_AspNetCore_Mvc_TagHelpers_RenderAtEndOfFormTagHelper;
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
            WriteLiteral("\n<script");
            BeginWriteAttribute("async", " async=\"", 185, "\"", 198, 1);
#nullable restore
#line 5 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
WriteAttributeValue("", 193, true, 193, 5, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            WriteLiteral("\n        src=\"https://telegram.org/js/telegram-widget.js?15\"\n        data-telegram-login=\"");
#nullable restore
#line 7 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
                        Write(Model.BotUserName);

#line default
#line hidden
#nullable disable
            WriteLiteral("\"\n        data-size=\"");
#nullable restore
#line 8 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
              Write(Model.ButtonStyle);

#line default
#line hidden
#nullable disable
            WriteLiteral("\"\n        ");
#nullable restore
#line 9 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
          
            if (!Model.ShowUserPhoto)
            {
                

#line default
#line hidden
#nullable disable
            WriteLiteral(" data-userpic=\"false\" ");
#nullable restore
#line 12 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
                                                   
            }
        

#line default
#line hidden
#nullable disable
#nullable restore
#line 15 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
          
            if (Model.CornerRadius != -1)
            {
                

#line default
#line hidden
#nullable disable
            WriteLiteral(" data-radius=\"");
#nullable restore
#line 18 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
                               Write(Model.CornerRadius);

#line default
#line hidden
#nullable disable
            WriteLiteral("\" ");
#nullable restore
#line 18 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
                                                                
            }
        

#line default
#line hidden
#nullable disable
#nullable restore
#line 21 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
          
            if (string.IsNullOrEmpty(Model.RedirectUrl))
            {
                

#line default
#line hidden
#nullable disable
            WriteLiteral(" data-onauth=\"onTelegramAuth(user, origin)\" ");
#nullable restore
#line 24 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
                                                                         
            }
        

#line default
#line hidden
#nullable disable
#nullable restore
#line 27 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
          
            if (string.IsNullOrEmpty(Model.RedirectUrl))
            {
                

#line default
#line hidden
#nullable disable
            WriteLiteral(" ");
#nullable restore
#line 30 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
                  Write(Model.RedirectUrl);

#line default
#line hidden
#nullable disable
            WriteLiteral(" ");
#nullable restore
#line 30 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
                                                 
            }
        

#line default
#line hidden
#nullable disable
#nullable restore
#line 33 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
          
            if (Model.SendMessageAccess)
            {
                

#line default
#line hidden
#nullable disable
            WriteLiteral(" data-request-access=\"write\" ");
#nullable restore
#line 36 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
                                                          
            }
        

#line default
#line hidden
#nullable disable
            WriteLiteral("></script>\n");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("form", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagAndEndTag, "96c40ad9078e7a56546dae0c6e69868074ccf9579311", async() => {
                WriteLiteral("\n    ");
#nullable restore
#line 40 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
Write(Html.AntiForgeryToken());

#line default
#line hidden
#nullable disable
                WriteLiteral("\n    <input type=\"hidden\"");
                BeginWriteAttribute("name", " name=\"", 1260, "\"", 1310, 1);
#nullable restore
#line 41 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
WriteAttributeValue("", 1267, TelegramLoginWidgetConstants.UserDataField, 1267, 43, false);

#line default
#line hidden
#nullable disable
                EndWriteAttribute();
                WriteLiteral(" id=\"userData\"/>\n    <input type=\"hidden\"");
                BeginWriteAttribute("name", " name=\"", 1352, "\"", 1400, 1);
#nullable restore
#line 42 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
WriteAttributeValue("", 1359, TelegramLoginWidgetConstants.OriginField, 1359, 41, false);

#line default
#line hidden
#nullable disable
                EndWriteAttribute();
                WriteLiteral(" id=\"origin\"/>\n");
            }
            );
            __Microsoft_AspNetCore_Mvc_TagHelpers_FormTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.TagHelpers.FormTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_TagHelpers_FormTagHelper);
            __Microsoft_AspNetCore_Mvc_TagHelpers_RenderAtEndOfFormTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.TagHelpers.RenderAtEndOfFormTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_TagHelpers_RenderAtEndOfFormTagHelper);
            __Microsoft_AspNetCore_Mvc_TagHelpers_FormTagHelper.Method = (string)__tagHelperAttribute_0.Value;
            __tagHelperExecutionContext.AddTagHelperAttribute(__tagHelperAttribute_0);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_1);
            BeginAddHtmlAttributeValues(__tagHelperExecutionContext, "action", 1, global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
#nullable restore
#line 39 "C:\Users\kruto\OneDrive\Desktop\universal_sales\Vepr-site\Vepr-site\Cackle.Identity.Telegram.UI\Areas\Identity\Pages\Account\TelegramLoginWidget.cshtml"
AddHtmlAttributeValue("", 1185, Model.CallbackPath, 1185, 19, false);

#line default
#line hidden
#nullable disable
            EndAddHtmlAttributeValues(__tagHelperExecutionContext);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral(@"
<script type=""text/javascript"">
    function onTelegramAuth(user, origin) {
        document.getElementById(""userData"").value = btoa(JSON.stringify(user));
        document.getElementById(""origin"").value = origin;
        document.getElementById(""telegramLogin"").submit();
    }
</script>");
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
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<Cackle.Identity.Telegram.UI.Areas.Identity.Pages.Account.TelegramLoginWidgetModel> Html { get; private set; }
    }
}
#pragma warning restore 1591

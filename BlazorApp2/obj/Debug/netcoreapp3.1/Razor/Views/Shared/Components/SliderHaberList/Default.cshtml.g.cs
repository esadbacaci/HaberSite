#pragma checksum "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\Views\Shared\Components\SliderHaberList\Default.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "30b0a627a7b1e0acfce59943ba1bd01932ef9fc6"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Shared_Components_SliderHaberList_Default), @"mvc.1.0.view", @"/Views/Shared/Components/SliderHaberList/Default.cshtml")]
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
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"30b0a627a7b1e0acfce59943ba1bd01932ef9fc6", @"/Views/Shared/Components/SliderHaberList/Default.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"a9af4978b9c2bfca24ef48e96efe5f8573634464", @"/Views/_ViewImports.cshtml")]
    #nullable restore
    public class Views_Shared_Components_SliderHaberList_Default : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<List<BlazorApp2.Models.Haber>>
    #nullable disable
    {
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_0 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("class", new global::Microsoft.AspNetCore.Html.HtmlString("img-fluid h-100"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_1 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("src", new global::Microsoft.AspNetCore.Html.HtmlString("~/layout/img/news-800x500-1.jpg"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_2 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("style", new global::Microsoft.AspNetCore.Html.HtmlString("object-fit: cover;"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_3 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("class", new global::Microsoft.AspNetCore.Html.HtmlString("img-fluid w-100 h-100"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_4 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("src", new global::Microsoft.AspNetCore.Html.HtmlString("~/layout/img/news-700x435-1.jpg"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_5 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("src", new global::Microsoft.AspNetCore.Html.HtmlString("~/layout/img/news-700x435-2.jpg"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_6 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("src", new global::Microsoft.AspNetCore.Html.HtmlString("~/layout/img/news-700x435-3.jpg"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_7 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("src", new global::Microsoft.AspNetCore.Html.HtmlString("~/layout/img/news-700x435-4.jpg"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
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
        private global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.UrlResolutionTagHelper __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper;
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
            WriteLiteral("\r\n<div class=\"container-fluid\">\r\n    <div class=\"row\">\r\n        <div class=\"col-lg-7 px-0\">\r\n            <div class=\"owl-carousel main-carousel position-relative\">\r\n");
#nullable restore
#line 7 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\Views\Shared\Components\SliderHaberList\Default.cshtml"
                 foreach (var item in Model)
                {

#line default
#line hidden
#nullable disable
            WriteLiteral("                    <div class=\"position-relative overflow-hidden\" style=\"height: 500px;\">\r\n                        ");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("img", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagOnly, "30b0a627a7b1e0acfce59943ba1bd01932ef9fc66444", async() => {
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.UrlResolutionTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_0);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_1);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_2);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\r\n                        <div class=\"overlay\">\r\n                            <div class=\"mb-2\">\r\n                                <a class=\"badge badge-primary text-uppercase font-weight-semi-bold p-2 mr-2\"");
            BeginWriteAttribute("href", "\r\n                               href=\"", 683, "\"", 722, 0);
            EndWriteAttribute();
            WriteLiteral(">");
#nullable restore
#line 14 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\Views\Shared\Components\SliderHaberList\Default.cshtml"
                                  Write(item.HaberCategory);

#line default
#line hidden
#nullable disable
            WriteLiteral("</a>\r\n                                <a class=\"text-white\"");
            BeginWriteAttribute("href", " href=\"", 802, "\"", 809, 0);
            EndWriteAttribute();
            WriteLiteral(">Jan 01, 2045</a>\r\n                            </div>\r\n                            <a class=\"h2 m-0 text-white text-uppercase font-weight-bold\"");
            BeginWriteAttribute("href", " href=\"", 953, "\"", 960, 0);
            EndWriteAttribute();
            WriteLiteral(">");
#nullable restore
#line 17 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\Views\Shared\Components\SliderHaberList\Default.cshtml"
                                                                                            Write(item.HaberTitle);

#line default
#line hidden
#nullable disable
            WriteLiteral("</a>\r\n                        </div>\r\n                    </div>\r\n");
#nullable restore
#line 20 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\Views\Shared\Components\SliderHaberList\Default.cshtml"
                }

#line default
#line hidden
#nullable disable
            WriteLiteral(@"            </div>
        </div>
        <div class=""col-lg-5 px-0"">
            <div class=""row mx-0"">
                <div class=""col-md-6 px-0"">
                    <div class=""position-relative overflow-hidden"" style=""height: 250px;"">
                        ");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("img", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagOnly, "30b0a627a7b1e0acfce59943ba1bd01932ef9fc69721", async() => {
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.UrlResolutionTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_3);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_4);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_2);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\r\n                        <div class=\"overlay\">\r\n                            <div class=\"mb-2\">\r\n                                <a class=\"badge badge-primary text-uppercase font-weight-semi-bold p-2 mr-2\"");
            BeginWriteAttribute("href", "\r\n                                   href=\"", 1638, "\"", 1681, 0);
            EndWriteAttribute();
            WriteLiteral(">Business</a>\r\n                                <a class=\"text-white\"");
            BeginWriteAttribute("href", " href=\"", 1750, "\"", 1757, 0);
            EndWriteAttribute();
            WriteLiteral("><small>Jan 01, 2045</small></a>\r\n                            </div>\r\n                            <a class=\"h6 m-0 text-white text-uppercase font-weight-semi-bold\"");
            BeginWriteAttribute("href", " href=\"", 1921, "\"", 1928, 0);
            EndWriteAttribute();
            WriteLiteral(@">Lorem ipsum dolor sit amet elit...</a>
                        </div>
                    </div>
                </div>
                <div class=""col-md-6 px-0"">
                    <div class=""position-relative overflow-hidden"" style=""height: 250px;"">
                        ");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("img", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagOnly, "30b0a627a7b1e0acfce59943ba1bd01932ef9fc612123", async() => {
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.UrlResolutionTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_3);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_5);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_2);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\r\n                        <div class=\"overlay\">\r\n                            <div class=\"mb-2\">\r\n                                <a class=\"badge badge-primary text-uppercase font-weight-semi-bold p-2 mr-2\"");
            BeginWriteAttribute("href", "\r\n                                   href=\"", 2520, "\"", 2563, 0);
            EndWriteAttribute();
            WriteLiteral(">Business</a>\r\n                                <a class=\"text-white\"");
            BeginWriteAttribute("href", " href=\"", 2632, "\"", 2639, 0);
            EndWriteAttribute();
            WriteLiteral("><small>Jan 01, 2045</small></a>\r\n                            </div>\r\n                            <a class=\"h6 m-0 text-white text-uppercase font-weight-semi-bold\"");
            BeginWriteAttribute("href", " href=\"", 2803, "\"", 2810, 0);
            EndWriteAttribute();
            WriteLiteral(@">Lorem ipsum dolor sit amet elit...</a>
                        </div>
                    </div>
                </div>
                <div class=""col-md-6 px-0"">
                    <div class=""position-relative overflow-hidden"" style=""height: 250px;"">
                        ");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("img", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagOnly, "30b0a627a7b1e0acfce59943ba1bd01932ef9fc614526", async() => {
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.UrlResolutionTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_3);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_6);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_2);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\r\n                        <div class=\"overlay\">\r\n                            <div class=\"mb-2\">\r\n                                <a class=\"badge badge-primary text-uppercase font-weight-semi-bold p-2 mr-2\"");
            BeginWriteAttribute("href", "\r\n                                   href=\"", 3402, "\"", 3445, 0);
            EndWriteAttribute();
            WriteLiteral(">Business</a>\r\n                                <a class=\"text-white\"");
            BeginWriteAttribute("href", " href=\"", 3514, "\"", 3521, 0);
            EndWriteAttribute();
            WriteLiteral("><small>Jan 01, 2045</small></a>\r\n                            </div>\r\n                            <a class=\"h6 m-0 text-white text-uppercase font-weight-semi-bold\"");
            BeginWriteAttribute("href", " href=\"", 3685, "\"", 3692, 0);
            EndWriteAttribute();
            WriteLiteral(@">Lorem ipsum dolor sit amet elit...</a>
                        </div>
                    </div>
                </div>
                <div class=""col-md-6 px-0"">
                    <div class=""position-relative overflow-hidden"" style=""height: 250px;"">
                        ");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("img", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagOnly, "30b0a627a7b1e0acfce59943ba1bd01932ef9fc616929", async() => {
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.UrlResolutionTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_3);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_7);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_2);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\r\n                        <div class=\"overlay\">\r\n                            <div class=\"mb-2\">\r\n                                <a class=\"badge badge-primary text-uppercase font-weight-semi-bold p-2 mr-2\"");
            BeginWriteAttribute("href", "\r\n                                   href=\"", 4284, "\"", 4327, 0);
            EndWriteAttribute();
            WriteLiteral(">Business</a>\r\n                                <a class=\"text-white\"");
            BeginWriteAttribute("href", " href=\"", 4396, "\"", 4403, 0);
            EndWriteAttribute();
            WriteLiteral("><small>Jan 01, 2045</small></a>\r\n                            </div>\r\n                            <a class=\"h6 m-0 text-white text-uppercase font-weight-semi-bold\"");
            BeginWriteAttribute("href", " href=\"", 4567, "\"", 4574, 0);
            EndWriteAttribute();
            WriteLiteral(">Lorem ipsum dolor sit amet elit...</a>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n\r\n\r\n");
        }
        #pragma warning restore 1998
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; } = default!;
        #nullable disable
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; } = default!;
        #nullable disable
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; } = default!;
        #nullable disable
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; } = default!;
        #nullable disable
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<List<BlazorApp2.Models.Haber>> Html { get; private set; } = default!;
        #nullable disable
    }
}
#pragma warning restore 1591

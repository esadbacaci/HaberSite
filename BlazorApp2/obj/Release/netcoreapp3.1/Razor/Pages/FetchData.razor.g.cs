#pragma checksum "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "e1464c0aa009ea489957194f3ed28139531c9e80"
// <auto-generated/>
#pragma warning disable 1591
namespace BlazorApp2.Pages
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Components;
#nullable restore
#line 1 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using System.Net.Http;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Authorization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Components.Authorization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Components.Forms;

#line default
#line hidden
#nullable disable
#nullable restore
#line 5 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Components.Routing;

#line default
#line hidden
#nullable disable
#nullable restore
#line 6 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Components.Web;

#line default
#line hidden
#nullable disable
#nullable restore
#line 7 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.JSInterop;

#line default
#line hidden
#nullable disable
#nullable restore
#line 8 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using BlazorApp2;

#line default
#line hidden
#nullable disable
#nullable restore
#line 10 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using BlazorApp2.Shared;

#line default
#line hidden
#nullable disable
#nullable restore
#line 11 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using BlazorApp2.Context;

#line default
#line hidden
#nullable disable
#nullable restore
#line 12 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.EntityFrameworkCore;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
using BlazorApp2.Models;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Components.RouteAttribute("/Admin/habers")]
    public partial class FetchData : OwningComponentBase<IHaberRepository>
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(global::Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
            __builder.AddMarkupContent(0, "<h1>Haber Listesi</h1>\r\n\r\n");
            __builder.AddMarkupContent(1, "<p>This component demonstrates fetching data from a service.</p>\r\n\r\n");
#nullable restore
#line 12 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
 if (HaberData == null)
{

#line default
#line hidden
#nullable disable
            __builder.AddContent(2, "    ");
            __builder.AddMarkupContent(3, "<p><em>Loading...</em></p>\r\n");
#nullable restore
#line 15 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"

}
else
{

#line default
#line hidden
#nullable disable
            __builder.AddContent(4, "    ");
            __builder.OpenElement(5, "table");
            __builder.AddAttribute(6, "class", "table");
            __builder.AddMarkupContent(7, "\r\n        ");
            __builder.AddMarkupContent(8, "<thead>\r\n            <tr>\r\n                <th>ID</th>\r\n                <th>Title</th>\r\n                <th>Desc</th>\r\n                <th>Category</th>\r\n                <th>Author</th>\r\n                \r\n            </tr>\r\n        </thead>\r\n        ");
            __builder.OpenElement(9, "tbody");
            __builder.AddMarkupContent(10, "\r\n");
#nullable restore
#line 31 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
             foreach (var hb in HaberData)
            {

#line default
#line hidden
#nullable disable
            __builder.AddContent(11, "                ");
            __builder.OpenElement(12, "tr");
            __builder.AddMarkupContent(13, "\r\n                    ");
            __builder.OpenElement(14, "td");
#nullable restore
#line 34 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
__builder.AddContent(15, hb.HaberId);

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
            __builder.AddMarkupContent(16, "\r\n                    ");
            __builder.OpenElement(17, "td");
#nullable restore
#line 35 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
__builder.AddContent(18, hb.HaberTitle);

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
            __builder.AddMarkupContent(19, "\r\n                    ");
            __builder.OpenElement(20, "td");
#nullable restore
#line 36 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
__builder.AddContent(21, hb.HaberDescription);

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
            __builder.AddMarkupContent(22, "\r\n                    ");
            __builder.OpenElement(23, "td");
#nullable restore
#line 37 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
__builder.AddContent(24, hb.HaberCategory);

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
            __builder.AddMarkupContent(25, "\r\n                    ");
            __builder.OpenElement(26, "td");
#nullable restore
#line 38 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
__builder.AddContent(27, hb.HaberAuthor);

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
            __builder.AddMarkupContent(28, "\r\n                    ");
            __builder.OpenElement(29, "td");
            __builder.OpenElement(30, "button");
            __builder.AddAttribute(31, "class", "btn btn-danger btn-sm");
            __builder.AddAttribute(32, "onclick", global::Microsoft.AspNetCore.Components.EventCallback.Factory.Create<global::Microsoft.AspNetCore.Components.Web.MouseEventArgs>(this, 
#nullable restore
#line 40 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
                                e => DeleteProduct(hb)

#line default
#line hidden
#nullable disable
            ));
            __builder.AddMarkupContent(33, "\r\n                        Delete\r\n                        ");
            __builder.CloseElement();
            __builder.AddMarkupContent(34, "\r\n                    ");
            __builder.CloseElement();
            __builder.AddMarkupContent(35, "\r\n                    ");
            __builder.OpenElement(36, "td");
            __builder.OpenElement(37, "a");
            __builder.AddAttribute(38, "class", "btn btn-info btn-sm");
            __builder.AddAttribute(39, "href", "/admin/habers/details/" + (
#nullable restore
#line 45 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
                                            hb.HaberId

#line default
#line hidden
#nullable disable
            ));
            __builder.AddMarkupContent(40, "\r\n                        Details\r\n                        ");
            __builder.CloseElement();
            __builder.AddMarkupContent(41, "\r\n                    ");
            __builder.CloseElement();
            __builder.AddMarkupContent(42, "\r\n                    ");
            __builder.OpenElement(43, "td");
            __builder.OpenElement(44, "a");
            __builder.AddAttribute(45, "class", "btn btn-warning btn-sm");
            __builder.AddAttribute(46, "href", "/admin/habers/edit/" + (
#nullable restore
#line 50 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
                                         hb.HaberId

#line default
#line hidden
#nullable disable
            ));
            __builder.AddMarkupContent(47, "\r\n                        Edit\r\n                        ");
            __builder.CloseElement();
            __builder.CloseElement();
            __builder.AddMarkupContent(48, "\r\n                ");
            __builder.CloseElement();
            __builder.AddMarkupContent(49, "\r\n");
#nullable restore
#line 54 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
            }

#line default
#line hidden
#nullable disable
            __builder.AddContent(50, "        ");
            __builder.CloseElement();
            __builder.AddMarkupContent(51, "\r\n    ");
            __builder.CloseElement();
            __builder.AddMarkupContent(52, "\r\n    ");
            __builder.OpenComponent<global::Microsoft.AspNetCore.Components.Routing.NavLink>(53);
            __builder.AddAttribute(54, "class", "btn btn-primary");
            __builder.AddAttribute(55, "href", "/admin/habers/create");
            __builder.AddAttribute(56, "ChildContent", (global::Microsoft.AspNetCore.Components.RenderFragment)((__builder2) => {
                __builder2.AddContent(57, "Create");
            }
            ));
            __builder.CloseComponent();
            __builder.AddMarkupContent(58, "\r\n");
#nullable restore
#line 58 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
}

#line default
#line hidden
#nullable disable
        }
        #pragma warning restore 1998
#nullable restore
#line 60 "C:\Users\bcces\Desktop\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
       



    public IHaberRepository haberRepository => Service;

    public IEnumerable<Haber> HaberData { get; set; }

    protected async override Task OnInitializedAsync()
    {
        await UpdateData();
    }

    public async Task UpdateData()
    {
        HaberData = await haberRepository.Habers.ToListAsync();
    }

    public async Task DeleteProduct(Haber p)
    {
        haberRepository.DeleteHaber(p);
        await UpdateData();
    }
    public string GetDetailsUrl(int id) => "/admin/habers/details/{id}";
    public string GetEditUrl(int id) => "/admin/habers/edit/{id}";

#line default
#line hidden
#nullable disable
    }
}
#pragma warning restore 1591

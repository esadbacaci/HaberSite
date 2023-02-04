// <auto-generated/>
#pragma warning disable 1591
#pragma warning disable 0414
#pragma warning disable 0649
#pragma warning disable 0169

namespace BlazorApp2.Pages
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Components;
#nullable restore
#line 1 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using System.Net.Http;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Authorization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Components.Authorization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Components.Forms;

#line default
#line hidden
#nullable disable
#nullable restore
#line 5 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Components.Routing;

#line default
#line hidden
#nullable disable
#nullable restore
#line 6 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.AspNetCore.Components.Web;

#line default
#line hidden
#nullable disable
#nullable restore
#line 7 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.JSInterop;

#line default
#line hidden
#nullable disable
#nullable restore
#line 8 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using BlazorApp2;

#line default
#line hidden
#nullable disable
#nullable restore
#line 10 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using BlazorApp2.Shared;

#line default
#line hidden
#nullable disable
#nullable restore
#line 11 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using BlazorApp2.Context;

#line default
#line hidden
#nullable disable
#nullable restore
#line 12 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\_Imports.razor"
using Microsoft.EntityFrameworkCore;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
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
        }
        #pragma warning restore 1998
#nullable restore
#line 60 "C:\Users\Mehmet\source\repos\BlazorApp2\BlazorApp2\Pages\FetchData.razor"
       



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

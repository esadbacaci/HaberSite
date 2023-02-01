using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using UniversityWeb.Models;


namespace UniversityWeb.ViewComponents.AnnouncementList
{
    public class AnnouncementList : ViewComponent
    {
        Context c = new Context();
        public IViewComponentResult Invoke()
        {
            var values = c.Announcements.ToList();
            values.Reverse();
            return View(values);
        }
    }
}

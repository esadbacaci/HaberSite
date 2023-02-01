using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using UniversityWeb.Models;

namespace UniversityWeb.Controllers
{
    public class AdminPanelController : Controller
    {
        Context c = new Context();
        public IActionResult Index()
        {
            var values = c.Announcements.ToList();
            values.Reverse();
            return View(values);
        }
        public IActionResult Delete(int id)
        {
            var values = c.Announcements.Find(id);
            c.Announcements.Remove(values);
            c.SaveChanges();
            return RedirectToAction("Index");
        }
        [HttpGet]
        public IActionResult Update(int id)
        {
            var val = c.Announcements.Find(id);



            return View(val);
        }

        [HttpPost]
        public IActionResult Update(AddImage announcement)
        {
            Announcement w = new Announcement();

            if (announcement.AnnouncementImg != null)
            {
                var extension = Path.GetExtension(announcement.AnnouncementImg.FileName);
                var newimagename = Guid.NewGuid() + extension;
                var location = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot/images/", newimagename);
                var stream = new FileStream(location, FileMode.Create);
                announcement.AnnouncementImg.CopyTo(stream);
                w.AnnouncementImg = newimagename;
            }
            w.AnnouncementTitle = announcement.AnnouncementTitle;
            w.AnnouncementDesc = announcement.AnnouncementDesc;

            w.AnnouncementID = announcement.AnnouncementID;
            c.Announcements.Update(w);
            c.SaveChanges();

            return RedirectToAction("Index");
        }


        [HttpGet]
        public IActionResult Add()
        {
            return View();
        }
        [HttpPost]
        public IActionResult Add(AddImage announcement)
        {

            Announcement w = new Announcement();
            if (announcement.AnnouncementImg != null)
            {
                var extension = Path.GetExtension(announcement.AnnouncementImg.FileName);
                var newimagename = Guid.NewGuid() + extension;
                var location = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot/images/", newimagename);
                var stream = new FileStream(location, FileMode.Create);
                announcement.AnnouncementImg.CopyTo(stream);
                w.AnnouncementImg = newimagename;
            }
                       w.AnnouncementTitle = announcement.AnnouncementTitle;
                       w.AnnouncementDesc = announcement.AnnouncementDesc;

            c.Announcements.Add(w);
            c.SaveChanges();
            return RedirectToAction("Index");
        }
    }
}

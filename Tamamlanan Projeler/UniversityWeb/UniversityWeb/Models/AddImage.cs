using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace UniversityWeb.Models
{
    public class AddImage
    {
        public int AnnouncementID { get; set; }
        public string AnnouncementTitle { get; set; }
        public string AnnouncementDesc { get; set; }
        public IFormFile AnnouncementImg { get; set; }

    }
}

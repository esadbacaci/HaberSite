using BlazorApp2.Models;
using Microsoft.EntityFrameworkCore;

namespace BlazorApp2.Context
{
    public class HaberDbContext:DbContext
    {
        //sorguları contexte kontrol ediyoruz
        //entityframework için gereklidir iletişimi sağlar
        public HaberDbContext(DbContextOptions<HaberDbContext> options) : base(options) { }

        public DbSet<Haber> habers { get; set; }
    }
}

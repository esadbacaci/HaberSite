using System.Linq;

namespace BlazorApp2.Models
{
    public interface IHaberRepository
    {//sorgulama işleri için kolaylık sağlar
        //havuz, servis ile bağlantı sağlar
        IQueryable<Haber> Habers { get; }

        void SaveHaber(Haber p);
        void CreateHaber(Haber p);
        void DeleteHaber(Haber p);

    }
}

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Sayfa_45_46_47_48_HesapMakinesi
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        decimal sayi1, sayi2, hafizadeger;
        Boolean sonuclandi;

        private void txt_sayi_giris_KeyPress(object sender, KeyPressEventArgs e)
        {
            //rakam girilmezse iptal et
            if (char.IsDigit(e.KeyChar)==false)
            {
                e.Handled = true;
            }
        }

        private void btn_artieksi_Click(object sender, EventArgs e)
        {
            if (txt_sayi_giris.Text.Length>0)
            {
                if (txt_sayi_giris.Text.Substring(0, 1) == "-")
                {
                    //sayi negatifse - kalkar poz hale gelir
                    //substring(1) ifadesi 1.elemandan sonrasını al demektir
                    txt_sayi_giris.Text = txt_sayi_giris.Text.Substring(1);
                }
                else
                {
                    //egersayi poz ise negatif hale getirilir 
                    //bunun icin txt_sayi_girisi kontrolünde ifadenin en solunda - eklenir.
                    txt_sayi_giris.Text = "-"+txt_sayi_giris.Text.Substring(0);
                }
            }
        }

        private void btn_ondalikvirgul_Click(object sender, EventArgs e)
        {
            if (txt_sayi_giris.Text.IndexOf(",") <= 0)
            {
                if (txt_sayi_giris.Text.Length == 0)
                {
                    //hic sayi girilmediyse 0 değerini atıyoruz
                    txt_sayi_giris.Text = "0";

                }
                else
                {
                    txt_sayi_giris.Text = txt_sayi_giris.Text + ",";

                }
            }
        }

        private void btn_CE_Click(object sender, EventArgs e)
        {
            hafizadeger = 0;

        }

        private void btn_C_Click(object sender, EventArgs e)
        {
            txt_sayi_giris.Text = "";
        }

        private void btn_gerial_Click(object sender, EventArgs e)
        {
            if (txt_sayi_giris.Text.Length>0)
            {
                txt_sayi_giris.Text = txt_sayi_giris.Text.Substring(0, txt_sayi_giris.Text.Length - 1);
            }
        }

        private void hafiza_islem(object sender, EventArgs e)
        {
            if (txt_sayi_giris.Text.Length==0)
            {
                txt_sayi_giris.Text = "0";

            }
            //hafıza işlemleriyle ilgili kodlar
            if ((sender as Button).Name=="btn_MC")
            {
                hafizadeger = 0;
                sonuclandi = true;

            }
            if ((sender as Button).Name == "btn_MR")
            {
                txt_sayi_giris.Text = hafizadeger.ToString();
                sonuclandi = true;

            }
            if ((sender as Button).Name == "btn_Marti")
            {
                hafizadeger = hafizadeger + Convert.ToDecimal(txt_sayi_giris.Text);
                sonuclandi = true;

            }
            if ((sender as Button).Name == "btn_Meksi")
            {
                hafizadeger = hafizadeger - Convert.ToDecimal(txt_sayi_giris.Text);
                sonuclandi = true;

            }

        }

    

        private void dort_islem(object sender, EventArgs e)
        {
            islem = (sender as Button).Name;
            if (txt_sayi_giris.Text.Length==0)
            {
                txt_sayi_giris.Text = "0";
            }
            sayi1 = Convert.ToDecimal(txt_sayi_giris.Text);
            sonuclandi = true;

        }

        private void btn_esittir_Click(object sender, EventArgs e)
        {
            sayi2 = Convert.ToDecimal(txt_sayi_giris.Text);
            decimal islem_sonucu = 0;

            if (islem=="btn_topla")
            {
                islem_sonucu = sayi1 + sayi2;
            }
            if (islem == "btn_cikar")
            {
                islem_sonucu = sayi1 - sayi2;
            }
            if (islem == "btn_carp")
            {
                islem_sonucu = sayi1 * sayi2;
                
            }
            if (islem == "btn_bol")
            {
                islem_sonucu = sayi1 / sayi2;
            }
            sonuclandi = true;
            txt_sayi_giris.Text = islem_sonucu.ToString();
        }

        private void diger_islemler(object sender, EventArgs e)
        {
            if (txt_sayi_giris.Text.Length==0)
            {
                txt_sayi_giris.Text = "0";
            }
            decimal diger_islemler_sayi = Convert.ToDecimal(txt_sayi_giris.Text);
            decimal sonuc = 0;
            if (((sender as Button).Name=="btn_karekok")&&diger_islemler_sayi>0)
            {
                sonuc = Convert.ToDecimal(Math.Sqrt((double)diger_islemler_sayi));
            }
            if ((sender as Button).Name=="btn_kare")
            {
                sonuc = diger_islemler_sayi * diger_islemler_sayi;
            }
            if ((sender as Button).Name=="btn_birbolu")
            {
                sonuc = 1 / diger_islemler_sayi;
            }
            txt_sayi_giris.Text = sonuc.ToString();
            sonuclandi = true;
        }

        string islem;

   

        private void rakam_girisleri(object sender, EventArgs e)
        {
            if (sonuclandi)
            {
                //hangi rakama aiy buttona basıldıysa onun üzerinde yazan sayı değeri alınıyor
                txt_sayi_giris.Text = (sender as Button).Text;
                sonuclandi = false;

            }
            else
            {
                //sayi girişi tamamlanmadıysa basılan rakamlar bir öncekininin sağ tarafına ekleniyor
                txt_sayi_giris.Text=txt_sayi_giris.Text+ (sender as Button).Text;

            }

        }
        
    }
}

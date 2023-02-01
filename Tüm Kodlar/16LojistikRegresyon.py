# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 09:58:22 2023

@author: SerdarKR
"""
"""
Kesikli veriler ile sınıflandırma yapılır bunu lojistik regresyon ile yapabiliriz.
 

Kategorik(Kalitatif, Nitel) Veri : Ölçülemeyen, üzerinden sayısal işlem yapılamayan nesnel verilerdir. Cinsiyet, saç rengi vb. nitel özellikleri belirten veriler.Nitel veriyle veri kümesindeki gözlemlere ilişkin sıfatlar ya da durumlar tespit edilir. Eğitim durumu, ev sahibi olup olmama gibi…Kategorik veriler nominal ve ordinal olmak üzere iki gruba ayrılır :

Sınıflanabilen (Nominal): Bir nominal niteliği ; gözlemlerin adları, yada sembolleri olarak düşünebiliriz. Bu değerler bir kategoriyi veya durumu temsil eder ve bu nedenle kategorik özellik olarak adlandırılırlar.Sınıfların aralarında hiyerarşik bir yapı yoktur. Araba markası, renk,meslek,il,cinsiyet gibi…

Sıralanabilen (Ordinal): Sıralayıcı nitel veriler aralarında anlamlı bir sıra veya derecelendirmeye sahip değerler içerir. Değerleri arasında sıralı bir ilişki bulunur. Akademik unvan, rütbe, öğrenim durumu,sınav notları gibi.



Numerik(Kantitatif,Nicel) Veri : Ölçülebilen, üzerinde aritmetik işlemler yapılabilen veri tipidir. Boy, kilo, hizmet süreleri, hava sıcaklığı, kandaki bir bileşenin miktarı… Nicel veriler kesikli ve sürekli olmak üzere iki şekilde incelenmektedir :

Discrete (Kesikli) Sayısal Veriler: Sonlu veya sayılabilir bir şekilde sonsuz değerler dizisine sahiptir. Gözlemlere ait özelliklerin tam sayılarla ifade edildiği veri kümeleridir. 0, 1, 2, 3 vb. tam sayı değerler…

Continious (Sürekli) Sayısal Veriler: Sonsuz sayıda değer alabilen ve kesirli değerleri de içeren veri setleridir.

7.00, 99.846, 200.1365 vb. değerler sürekli verilere örnek verilebilir

Aralıklı (Interval): Hem sırayı hem de farkı gösterir. Eşit aralıkların eşit mesafeleri temsil ettiği bir ölçek türüdür. Sayılar arasında oransal bir ilişki yoktur.

Sıcaklık bunun için iyi bir örnektir. 25°C ile 30°C arasındaki fark, 40 °C ile 45 °C arasındaki farkla aynıdır.

Aralık değişkenleri ile ilgili en önemli nokta, mutlak bir sıfır noktası bulunmamasıdır.Örneğin, 0°C sıcaklığı, havada hiç sıcaklık olmadığı anlamına gelmez!

Oranlı (Ratio): Sırayı, mesafeyi ve anlamlı bir mutlak sıfır değerini gösterir. Bir oran değişkeni 0 değerine sahip olduğunda, değişken tarafından ölçülen miktarın hiçbirinin mevcut olmadığını anlarız.

Örnek olarak, yaş bir oran değişkenidir: 0 yaşında biri henüz doğmamıştır ve 20 yaşında biri 10 yaşında birinin iki katı yaşamıştır.



Binary Lojistik regresyonda hedefin 0 yada bir olduğu durumlarda uygulanır örneğin müşteriye kredi ver yada verme?
Resimler klasöründe LinearRegresyonKesikliVeriHatası resmine bakınız

Lojistik Regresyon Çeşitleri için resimler klaösrüne bakınız
Veri Seti:
    train_kredi_tahmini
    test_kredi_tahmini
    
Örenk Kodlar=https://www.kaggle.com/code/colecola/kredi-tahmini-1

eksik verileri tamamla kolonlarını yeniden isimlenidir hepsini sayısal veriye dönüştür ve sonra ölçeklendir.

Education(Egitim_Durumu) için:
    graduate :1
    not graduate:0
    
Gender(Cinsiyet):
    Male  :0
    Female:1

Married(Medeni_Hali):
    Yes:1
    No:0
LoanID: Silinecek

Dependents(CocukSayisi):Sayısala Dönüşecek Ordinal

SelfEmployed(Patron): 
    Yes:1
    No:0
ApplicantIncome(GelirDuzeyi):Olduğu Gibi Kalacak

CoapplicantIncome(EkGelirDuzeyi):Olduğu Gibi Kalacak

LoanAmount(KrediMiktarı):Olduğu Gibi Kalacak
     
Loan_Amount_Term(KrediVadesi):Olduğu Gibi Kalacak

Credit_History(OncedenKrediAlmismi):Olduğu Gibi Kalacak

Property_Area(one hot encode): Urban=Kentsel rural=Kırsal semiurban=Yarı_kentsel

Loan_Status(KrediyeUygun): 
    Bu alan y olarak farklı bir dataframe olacak 
    ve bu tahmin ettirilecek eğitim  ve tets dataframe'inden çıkarılacak
    Yes:1
    No:0
Ölçeklendir bütün 0 veya 1 arasında olmayanları 0 ve 1 arasına ölçeklendir. 
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
import boslukdolduryeni as bd
import ordveolceklendirme as olck
import encoding as ec
import normstandrt as nmstd

df=pd.read_csv("train_kredi_tahmini.csv")

thisdict={}
listkeys=list(df.columns)
listvalues=["KrediID","Cinsiyet","Medeni_Hali","CocukSayisi","Egitim_Durumu","Patron",
            "GelirDuzeyi","EkGelirDuzeyi","KrediMiktarı","KrediVadesi",
            "OncedenKrediAlmismi","Property_Area","KrediyeUygun"]
thisdict = {listkeys[i]: listvalues[i] for i in range(len(listkeys))}
#Kolonların Sisimlerini Tekrar Düzenle
df.rename(columns=thisdict,inplace=True)

#Boşlukları Doldru
bd.boslukdoldurdf(df)#boslukların stringler için mode intler için ortalaması

#Verileri Ordinal Hale Getir.
olck.ordinalveri2(df, "CocukSayisi", {'0':0, '1':1, '2':2, '3+':3})
olck.ordinalveri(df,"Cinsiyet", {"Male":1,"Female":0})
olck.ordinalveri(df, "Egitim_Durumu", {"Graduate":1,"Not Graduate":0})
olck.ordinalveri(df, "Patron", {"Yes":1,"No":0})
olck.ordinalveri(df, "Medeni_Hali", {"Yes":1,"No":0})


#İlgili Alanlar İçin Encoding Yap.
ec.encoding(df, ["Property_Area"])
df.drop("KrediID",axis="columns",inplace=True)
df.rename(columns={"Urban":"Kentsel","Rural":"Kırsal","Semiurban":"Yarı_kentsel"},inplace=True)
#Gerekli Alanlara Normalizasyon Uygula
nmstd.minmaxnorm(df, ["GelirDuzeyi","EkGelirDuzeyi","KrediMiktarı","KrediVadesi"])

#Data seti x ve y olarak ayır
x=df.drop("KrediyeUygun",axis="columns")
y=df["KrediyeUygun"]


# Eğitim Ve Test Setini Ayır
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)#alt kümler her seferinde aynı olacak şekilde

print(X_train.shape)
print(X_test.shape)

#Model Kur
model=LogisticRegression(random_state=0)
#Modeli Eğit
model.fit(X_train,y_train)

#Tahmin işlemi
y_predict=model.predict(X_test)


#Performans Değerlendirmesi

#confisuon matris ile yapılır çünkü kesikli veri

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

confusion_matrix(y_true=y_test,y_pred=y_predict)#bunun sonucu bize bir 2 darray verir
classification_report(y_true=y_test,y_pred=y_predict)

accuracy_score(y_true=y_test,y_pred=y_predict)
















 

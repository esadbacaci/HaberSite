# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:46:09 2022

@author: SerdarKR
"""
#https://www.youtube.com/watch?v=7iCWoxFGJyw hesaplama için gerekli
#sınıflandrıma kesikli veriler söz konusu ise örneğin bir el yazısı ile rakam tahmini yapılacak sonuc 1 yada 9 diğer durumlarda regresyon yapılır
# regresyon ise örneğin bir muhitteki ev fiyatları 1 ile 5 milyon arasında değişen değerler ise bu zamanda regresyon analizi yapmamız gerekecek
#lineer regresyon bağımlı değişken y ile bağımsız değişken x arasındaki ilişkinin fonksiyonel biçimi 
#veriyi lineer bir çizgiye uydurma y nin x e göre nasıl değiştiği ve yeni x e göre y nin ne olacağının ortaya konulması amacıdır
#linear regresyon doğrusal regresyon bir değişkenin değerinin bağımlı tek değişkene göre  linear bir fonksiyona uydurma işlemi için yani tek değerli
#lojistik regresyon binary veri 1 yada 0 gördüğümüz veya 0 dan 9 a kadar olan sayıların ssınıflandırılması gibi sınıflandırma için kullanılabilir.
#


#basit linear regresyon tek değişkenli y=mx+n +hata şeklinde çözüm sağlayan modele denir
#bağımsız değişken birden fazla uydurmaya çalıştığımız formül doğru ise çoklu linear regresyon tek bağımsız değişken ise basti linear regresyon deriz.  
#1 sürekli verilerde çalışır
#2 kategorik verilerde çalışmaz.
#3 toplam hatayı minimize etmeye çalışılır
#Regresyon standart hatası ne kadar küçük olursao kadar doğru bir çizgi çizmiş oluruz
#determinasyon katsayısı da başarı ölçüsüdür
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


satislar=np.array([22,21,23,26,30,31,32])
reklam_giderleri=np.array([7,11,15,22,26,28,31])
df=pd.DataFrame({"Satis":satislar,"ReklamGiderleri":reklam_giderleri})
print(df.head())

df.index=["2000","2001","2002","2003","2004","2005","2006"]
print(df)
yillar=[str(x+2010) for x in range(7)]
df.index=yillar
plt.figure(0)
plt.scatter(df.ReklamGiderleri,df.Satis)
plt.xlabel("Reklam Giderleri")
plt.ylabel("Satış Rakamları")
plt.plot(df.ReklamGiderleri,df.ReklamGiderleri*1+3,color="red")
plt.show()


df.ReklamGiderleri
linearmodel=LinearRegression()
linearmodel.fit(np.array(df.ReklamGiderleri).reshape(-1,1),np.array(df.Satis).reshape(-1,1))#reshape(-1,1) satır sayısı önemli değil sütun sayısı 1 olsun çükü girdileri tablo görünümü istiyor
print(linearmodel.coef_)#katsayilar mx + n in m i diyebiliriz
print(linearmodel.intercept_)#buda mx + n'in n+i diyebiliriz
#determinasyon katsayısı
print(linearmodel.score(np.array(df.ReklamGiderleri).reshape(-1,1),np.array(df.Satis).reshape(-1,1)))

satislar_tahmin=linearmodel.predict(np.array(df.ReklamGiderleri).reshape(-1,1))
teksatis_tahmin=linearmodel.predict(np.array([11]).reshape(-1,1))
teksatis_tahmin2=linearmodel.predict([[11]])
satislar_reel=np.array(df.Satis).reshape(-1,1)
hatalar=satislar_reel-satislar_tahmin
hatalarkare=np.square(hatalar)
hatalarkare=hatalar**2
#r_2=1-u/v
#u= hatalarkare toplamı
u=hatalarkare.sum()
v=((df.Satis-df.Satis.mean())**2).sum()
r_2=1-(u/v)
       
plt.figure(1)
plt.scatter(df.ReklamGiderleri,df.Satis,color="red",label="Gerçek Değerler")
plt.xlabel("Reklam Giderleri")
plt.ylabel("Satış Rakamları")
plt.plot(df.ReklamGiderleri,satislar_tahmin,color="blue",label="Tahmin Değerleri")
plt.title("Reklam Satış İlişkisi")
plt.legend()
plt.show()


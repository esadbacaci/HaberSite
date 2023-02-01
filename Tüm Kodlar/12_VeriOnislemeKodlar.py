# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:14:37 2022

@author: SerdarKR
"""

import pandas as pd
from matplotlib import pyplot as plt
import bosluktemizle as bt
import boslukdolduryeni as bdyeni
import aykiriveri as av


df=pd.read_csv("eksikveriler2.csv")
df["yas"].plot(kind="box")
plt.boxplot(df["yas"])
plt.boxplot(df["boy"])
plt.boxplot(df["kilo"])

df.ulke.dtypes
df.describe()
df.dtypes

df1=bt.temizle("eksikveriler2.csv")

df2=bdyeni.boslukdoldur("eksikveriler2.csv", 1)

df3=av.aykiriveridoldur(df2,1)

df2=bdyeni.boslukdoldur("eksikveriler2.csv", 1)
df4=av.aykiriveridoldur(df2,1,1)#ortalamadan std kadar geri ve ileri olanlar harici
df2=bdyeni.boslukdoldur("eksikveriler2.csv", 1)
df5=av.aykiriveridoldur1(df2,1)#iqr değerlerine göre 1.5 iqr q3 den uzak 1.5 iqr q1den uzak veriler için

df2=bdyeni.boslukdoldur("eksikveriler2.csv", 1)
df6=av.aykiriveridoldur2(df2,1)# verinin yüzde 95 i ortalamadan 1.96 std sapma kadar ileride ve geride dir

df2=bdyeni.boslukdoldur("eksikveriler2.csv", 1)
df7=av.aykiriveridoldur3(df2,["yas"],1,1.5)# zscore larına göre
# z score ortalamadan kaç standart sapma gidilmiş?
#labelencoding ve one hot encoding
import encoding as ec
ec.encoding(df7,["cinsiyet","ulke"])


plt.figure(2)
x=df5["yas"]
plt.hist(x, 100)
plt.show()

import ordveolceklendirme as olck

df8=olck.ordinalveri(df6.copy(),"ulke", {"tr":1,"fr":2,"us":3})


df9=olck.ordinalveri2(df6.copy(),"ulke", {"tr":1,"fr":2,"us":3})

df10=olck.kesikli(df6.copy(), "boy", {"ckisa":130,"kisa":150,"orta":170,"uzun":190,"cuzun":210},str)
#dict teki valuelar küçükten büyüğe olmalı




# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:19:50 2022

@author: SerdarKR
"""
import pandas as pd

dict1={"Ad":["Serdar","Ahmet","mehmet","ZEYNEP","Ali Kemal","Kasım"],
       "Yas":[17,15,22,40,60,55],
       "Maas":[150,170,140,250,200,180]
       }
df1=pd.DataFrame(dict1)

print(df1.head())
print(df1.tail())

kolonlari=df1.columns

for each in kolonlari:
    print(each)
print(df1.info())

bilgi=df1.info()
print(df1.dtypes)

datatipler=df1.dtypes

print(df1.describe())

description = df1.describe()

print(df1.Ad)

print(df1["Ad"])

df1["yeni özellik"]=[-6,-5,-4,-3,-2,-1]

print(df1["yeni özellik"])

print(df1["Yas"])
pdserisi1=df1["Yas"]#referans

print(df1.loc[:,"Yas"])
##burda copy() kopyasını oluşturur
pdserisi2=df1.loc[:,"Yas"].copy()

pddataframe1=df1.loc[:,["Yas"]]

print(df1.loc[::-1,:])

pddataframe2=df1.loc[::-1,:]

print(df1.loc[:,::-1])


print(df1.loc[:3,:])
print(df1.loc[:3,"Ad":"Maas"])
print(df1.loc[:3,:"Maas"])

print(df1.loc[:,["Maas","Ad"]])

print(df1.iloc[:3,1:4])

#filitreleme

filtre=df1.Maas>150

print(df1[filtre])

filtre2=df1.Yas>18
print(df1[filtre2])

print(df1[filtre &filtre2])

print(df1[df1.Maas<180])

import numpy as np

ortalama_maas=np.mean(df1.Maas)

ortalama=df1.Maas.mean()
liste=[]
for each in df1.Maas:
    if(each<ortalama):
        print("Düşük")
    else:
        print("Yüksek")
df1["Maas Seviyesi"]=["Düşük" if each<ortalama else "Yüksek" for each in df1.Maas]

for each in df1.Maas:
    if(each<ortalama):
        liste.append("Düşük")
    else:
        liste.append("Yüksek")

df1["Maas Seviyesi"]=liste

print(df1.columns)

df1.columns=[each.lower() for each in df1.columns]

df1.columns=[each.split()[0]+"_"+each.split()[1] if len(each.split())>1 else each for each in df1.columns]
#drop

df1.drop(["yeni_özellik"],axis=1,inplace=True)

#concat

df1h=df1.head()
df1t=df1.tail()

df_concat=pd.concat([df1h,df1t],axis=0)

df1_concat=pd.concat([df1h,df1t],axis=1)

maas=df1.maas
yas=df1.yas

df1h=pd.concat([maas,yas],axis=1)
print(df1.describe())


df1["maasartir"]=[each*2 for each in df1.maas]

def artir(maas):
    return maas*2

df1["maasartir2"]=df1.maas.apply(artir)


def kucult(ad):
    return ad.lower()

df1["ad"]=df1.ad.apply(kucult)

def temizle(ad):
    return ad.replace(" ","")
df1.ad=df1.ad.apply(temizle)

df1.ad=[each.split()[0]+"_"+each.split()[1] if len(each.split())>1 else each for each in df1.ad]

def birlestirkucult(ad):
    ad=ad.lower()
    if len(ad.split())>1:
        return ad.split()[0]+"_"+ad.split()[1]
    else:
        return ad
    
df1.ad=df1.ad.apply(birlestirkucult)










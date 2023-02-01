# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:36:42 2023

@author: SerdarKR
"""

"""
K= 3

G1 G2 Ç
4  3  F
4  7  P
7  8  P
5  5  F
8  8  P
tahmin edilecek 7,8 

Uzaklık Hesaplama Oklit'e göre hesaplanacak

3 komşudan en yakınına bakılacak

parametre ekleyin çıktısının sayısı gönderilecek çıktı sayısı artı 1 kadar k değeri seçilecek


2. si ise dataframe'in çıktı saysının 
Unique length 

Tahmin delecek verinin özellikleri yollanacak ve df yollanacak
bana hangi sınıfta olduğu dönecek.

"""
import pandas as pd

from Siniflandirma import KNNSiniflandirma

liste=[[4,3,"F"],[4,7,"P"],[4.1,7.1,"P"],[7,8,"N"],[5,5,"F"],[8,8,"P"],[8,8,"T"],[4,3,"F"],[4,7,"P"],[4.1,3.1,"F"],[4,7,"P"]]
df1=pd.DataFrame(liste)

df1.columns=["G1","G2","Ç"]

X=df1[["G1","G2"]]
Y=df1[["Ç"]]

data={"G1":[4,4],"G2":[3,7]}
X_Test=pd.DataFrame(data)
Y_Test=df1.loc[:1,["Ç"]]
#Uzaklık=KNNSiniflandirma(X, Y, X_Test,KSayisi=7)
Y_Predict=KNNSiniflandirma(X, Y, X_Test)

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

confusion_matrix(y_true=Y_Test,y_pred=Y_Predict)#bunun sonucu bize bir 2 darray verir

classification_report(y_true=Y_Test,y_pred=Y_Predict)
accuracy_score(y_true=Y_Test,y_pred=Y_Predict)








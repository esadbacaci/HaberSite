# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 15:38:00 2023

@author: SerdarKR
"""
#class SiniflandirmaKNN:
import math
import pandas as pd
from statistics import mode 

def KNNSiniflandirma(X_Train,Y_Train,X_Test,KSayisi=0):#k veri setinin uzunluğundan büyük olamaz
    
    liste=[]
    for sirayla in X_Test.index:
        print(str(sirayla)+".satır")
        liste.append(KNNSiniflandirma1(X_Train,Y_Train,X_Test.iloc[[sirayla]].reset_index(),KSayisi))
        print("\n")
    Sonuc=pd.DataFrame(liste,columns=Y_Train.columns)  
    return Sonuc


def KNNSiniflandirma1(X_Train,Y_Train,X_Test,KSayisi=0):
    if KSayisi==0:
        KSayisi=KBelirle(Y_Train) 
  
    UzaklikDict={}
    
    for satirlar in X_Train.index:        
        Uzaklik=0        
        for sutunlar in X_Train.columns:
            Uzaklik+=pow((X_Train[sutunlar][satirlar]-X_Test[sutunlar][0]),2)
        Uzaklik=math.sqrt(Uzaklik)
        UzaklikDict[Uzaklik]=Y_Train.iloc[satirlar,0]  
    
    return  eniyisonuc(UzaklikDict,KSayisi)

def KBelirle(Y_Train):
    kSayisi=len(Y_Train.iloc[:,0].unique())
    kSayisi+=1
    print("K Sayisi:"+str(kSayisi))
    return kSayisi

def eniyisonuc(UzaklikDict,KSayisi):
       
    Keyler = list(UzaklikDict.keys())
    Keyler.sort()
    siralisozluk = {i: UzaklikDict[i] for i in Keyler}
    encoktekrar=mode(list(siralisozluk.values())[0:KSayisi])
    print("Sirali Sozluk: ")
    print(siralisozluk)
    print("En Çok Tekrar Eden: "+encoktekrar)
    
    return encoktekrar
    
    
    

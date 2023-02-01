# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:04:18 2022

@author: SerdarKR
"""
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
liste=[1,2,3,4]
class calisan:
    sayac=0 
    zamorani=0.5
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        calisan.sayac+=1
    def zamyap(self):
        self.maas=self.maas+(self.maas*self.zamorani)
        
def Yaz(name):
    """
    

    Parameters
    ----------
    name : TYPE
        Ne yollarsan yazarım.

    Returns
    -------
    None.

    """
    print(name)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:36:44 2022

@author: SerdarKR
"""

class Sinif1:
  x = 5

n1=Sinif1()
print(Sinif1.x)
print(n1.x)

class Sinif2:
    pass

class Sinif3:
    y=7    
    def __init__(self):
        self.x=5

n2=Sinif3()
print(n2.x)
print(n2.y)

x=10

class Sinif4:
    global x
    x=100
    y=7    
    def __init__(self):
        self.x=5
        self.y=10

n4=Sinif4()
print(n4.x)
print(n4.y)
print(Sinif4.y)



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
        
c1=calisan("serdar","kr",1000)
c2=calisan("Elif","kr",1000)
c3=calisan("Yusuf","kr",1000)

calisan.zamorani=2
c2.zamyap()
print(c2.maas)

c1.zamyap()
print(c1.maas)

c3.zamorani=1.5
c3.zamyap()


xx=100

class sinif7:
    global xx
    xx=10
    def __init__(self):
        self.xx=15


n1=sinif7()
print(n1.xx)
print(xx)





























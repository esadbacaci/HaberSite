# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:09:52 2022

@author: SerdarKR
"""

#list tuple set dictionaries
#if koşulllar

x=100
y=6

liste=[1,2,3,4,5]
liste2=[11,22,33,24,55]
if x==y:
    print("x eşit y")
    print("sdfasdfa")
else:
    print("x eşit değil y")
    print("sdfasdfa")

if x in liste:
    print("x listede var")
elif x in liste2:
    print("x liste 2 de")
else:
    print("hiç yok")
   
if x>=100:
    pass
print("sdfsd")

if x>100: print("x 100den büyük") 
print("x 100den büyük ") if x>100 else print("x küçüktür 100")
print("x 100den büyük ") if x>100 else print("x 100dür") if x==100 else print("100 den küçük")     
  
#%%
#while loop
i=0
while(i<100):
    print(i)
    i+=1
degisken=input("sayi girin")
print(type(degisken))
degisken =int(degisken) 

bas=int(input("başlangici gir"))
bit=int(input("bitiş"))

mod=int(input("mod alınacak sayi"))

while bas<bit:
    if bas%mod==0 and bas!=0:
        bas+=1
        continue
    print(bas)
    bas+=1
i=200
while i>0:
    if i%14==0:
        print(i)
        print(i/14)
        break
    i-=1

yeniliste = [x for x in range(0,100)]

liste1=[]
for j in range(0,100):
    liste1.append(j)
    
    
liste2=[x for x in range(0,100) if x%7!=0]    
liste3=[x if x%7!=0 else "yedinin katı" for x in range(0,100)]   
liste4=["yedinin katı" if (x%7==0 and x!=0) else x for x in range(0,100)]      
    
   
import random as rnd
liste5=[]
for x in range(100):
    liste5.append(rnd.randrange(0,10))    
   
alt=int(input("alt limit"))
ust=int(input("ust limit"))
dizilen=int(input("dizi uzunluğu"))
aranan=int(input("ararnan deger?"))

liste6=[]
for x in range(0,dizilen):
    liste6.append(rnd.randrange(alt,ust))
listeindeks=[]
for x in range(0,dizilen):
    if liste6[x]==aranan:
        listeindeks.append(x)
print("aranan eleman {0} adet var",len(listeindeks))
print(listeindeks)        


    
   
    
   
    
   
    
   
    
   
    
   
    
   














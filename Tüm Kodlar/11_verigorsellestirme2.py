# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 23:31:22 2021

@author: SerdarKR
"""
import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([1,4, 8])
ypoints = np.array([3,4, 10])

plt.figure(0)
plt.plot(xpoints, ypoints)
plt.show()


x=np.linspace(-np.pi,np.pi,100)
y=np.sin(x)
plt.figure(1)
plt.plot(x,y,label="sinüs")
y=np.cos(x)
plt.plot(x,y,label="cosinüs")
plt.legend()
plt.figure(1).savefig("sincos.svg")


x=np.linspace(-np.pi,np.pi,100)
y=np.sin(x)
fig2=plt.figure(2)
plt.plot(x,y,label="sinüs")
y=np.cos(x)
plt.plot(x,y,label="cosinüs")
plt.legend()
fig2.savefig("cossin.svg")

plt.ion()

for i in range(20):
    x=np.linspace(-np.pi+i*0.1,np.pi+i*0.1,100)
    y=np.sin(x)
    plt.plot(x,y)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

plt.style.use("ggplot")

for each in range(20):   
    plt.ion()
    x=np.linspace(-np.pi,np.pi,each)
    y=np.sin(x)
    plt.plot(x,y)
    plt.draw()
    plt.pause(0.5)
    plt.clf()

#bar plot
np.random.seed(12345)
x1_koor=np.random.randint(10,size=20)
y1_koor=np.random.randint(5,size=20)

x2_koor=np.random.randint(10,size=20)
y2_koor=np.random.randint(5,size=20)
   
plt.bar(x1_koor,y1_koor,label="1.koor")
plt.bar(x2_koor,y2_koor,label="2.koor")
plt.legend(loc=0)  

x=np.arange(3)
plt.bar(x,height=[1,2,3])
plt.xticks(x,["a","b","c"])
 
#3 adet float 
rasgelefloat=np.random.rand(3) 
#2 ye 3 boyutlu
rasgeleboyutlu=np.random.rand(2,3)
plt.show()

#0 ile 2 arası rasgele tek sayi
rasgeleint=np.random.randint(3)
#rasgele çok sayi
rasgelecoksayi=np.random.randint(low=0,high=100,size=100)
#rasgeleçok boyutlu sayi
rasgelecokboyut=np.random.randint(1,10,size=[2,3])

np.random.seed(12345)
kadin_yas= np.random.randint(low=20,high=70,size=100)
erkek_yas=np.random.randint(low=18,high=65,size=100)
plt.hist(kadin_yas,label="kadinlar")
plt.hist(erkek_yas,label="erkekler")
plt.legend()

#normal dağılım için
xnormal=np.random.normal(loc=50,scale=10,size=1000)
plt.hist(xnormal)
plt.figure()
plt.hist(xnormal,density=True)
plt.figure()
plt.hist(xnormal,density=True,bins=50)

#bir tane soru işaeti var 
import pandas as pd
hdesase=pd.read_csv("heart.csv","x")
print(hdesase.dtypes)
print(hdesase.dtypes[7])#object dönüyor ancak veriler sayısal
print(type(hdesase.maxheartrate[1]))
import kolonduzenle as kd
kd.kolonduzenle(hdesase,["maxheartrate"],int)##df yolla ve kolon yolla ve dönüştürülecek veri biçimin yoll

plt.boxplot(hdesase["maxheartrate"])

print(hdesase["maxheartrate"][0])

import aykiriveri as av
av.aykiriveridoldur3(hdesase,["maxheartrate"], 1)

plt.boxplot(hdesase["maxheartrate"])
plt.plot(hdesase.maxheartrate)
plt.plot(hdesase.maxheartrate[0:100])

fig3=plt.figure()
fig3.show()
ax=plt.axes()
fig3.show()

fig4,ax=plt.subplots(2,1)
fig4.set_facecolor("red")
x=[2,5,3]
y=[4,6,10]
xx=[1,2,3,4]
yy=[12,213,33,66]
ax[0].plot(x,y)
ax[1].plot(xx,yy)

fig,ax=plt.subplots(2,2,figsize=(10,10))
ax[0,0].text(0.5,0.5,"Birinci Hücre")


xlist = np.linspace(-3.0, 3.0, 10)
ylist = np.linspace(-3.0, 3.0, 10)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)
fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()










  


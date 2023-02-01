# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:17:59 2022

@author: SerdarKR
"""

f = open("myfile.txt", "x")
f.write("fdsfsd")
f.close()
f=open("myfile.txt", "a")
f.write("\nfdsdf")
f.close()
f=open("myfile.txt", "r")
print(f.read(15))
f.close()
#%%numpy

import numpy as np
array =np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
kacboyut=array.ndim
uzunluk=len(array)
print(array.shape)
bicimi=array.shape
print(len(array.shape))



array2=array.reshape(4,4)
print(array2.shape)
bicim2=array2.shape
print(bicim2[0])
print(bicim2[1])
print(array2.ndim)
uzunluk2=len(array2)
print(len(array2.shape))

print(array2[1,2])


print(array2[1][2])

array3=array.reshape(4,2,2)

print(array3.shape)
print(array3.ndim)
print(array3.shape[2])
print(len(array3.shape))
print(len(array3))
print(array3[0,0,1])
print(array3.size)

print(array3[2,0,1])

array4=array3.reshape(array3.size)

print(array4.dtype.name)

#%%

liste=[1,2,3,4,5,6,7,8]

npdizi=np.array(liste)

npdizi=npdizi.reshape(4,2)
print(type(npdizi))

sifirdizisi=np.zeros((4,4))
birlerdizisi=np.ones((4,4))
bosdizi=np.empty((3, 3))#4 satır yada sütun için 1 rakamı

arrangedizi=np.arange(0,100,5)
lindizi=np.linspace(0,100,26)

a=[1,2,3,4,5]
b=[1,2,3,4,5]

aa=np.array(a)
bb=np.array(b)

print(aa)
print(bb)

print(aa+bb)

print(aa*2)
print(aa-2)

print(aa*bb)

print(aa**bb)
print(aa**2)


print(np.sin(aa))

x=np.array([[1,2,3,4],
            [1,2,3,4]])

y=np.array([[1,2,3,4],
            [1,2,3,4]])

#(2,4) (2,4)=>2,2
print(x+y)

print(y.T)

xy=x.dot(y.T)

print(np.exp(xy))

randommatris=np.random.random((4,5))

print(randommatris.sum())
print(randommatris.max())

print(randommatris.min())

print(randommatris.sum(axis=0))#sütunların toplamı
print(randommatris.sum(axis=1))#sütunların toplamı

print(np.sqrt(randommatris))
print(np.square(randommatris))



print(np.add(x,y))



#%%
import numpy as np
liste=[1,2,3,4,5,6,7,8]
liste2=[11,22,33,44,55,66,77,88]

npdizi=np.array(liste)
npdizi2=np.array(liste2)

print(npdizi[:])

print(npdizi[:-1])
print(npdizi[1:-1])
print(npdizi[2:])
print(npdizi[-5:])

dikeybir=np.vstack((npdizi,npdizi2))
yataybir=np.hstack((npdizi,npdizi2))

dikeybir1=np.row_stack((npdizi,npdizi2))
yataybir1=np.column_stack((npdizi,npdizi2))

dikey2=np.stack((npdizi,npdizi2),axis=-1)
yatay2=np.stack((npdizi,npdizi2),axis=0)


print(dikeybir.ndim)
print(dikeybir.shape)

yataybir.resize(4,4)
duzeltilmis=yataybir.ravel()

print(yataybir[:,:])

print(yataybir[:,:-1])


print(yataybir[:-1,:])


print(yataybir[:,:])


print(yataybir[1:3,1:])


print(yataybir[1:,2])






















































































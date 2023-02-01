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

plt.figure(1)
plt.plot(xpoints, ypoints,'o')
plt.show()



ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.figure(2)
plt.plot(ypoints)
plt.show()

plt.figure(3)
plt.plot(ypoints,marker='*')
plt.show()

#marker|line|color format string 
#https://www.w3schools.com/python/matplotlib_markers.asp
ypoints = np.array([2, 6, 1, 9, 4, 8])
plt.figure(4)
plt.plot(ypoints,'*:r')# yıldız noktalı kırmızı
plt.show()


plt.figure(3)
plt.plot(ypoints,'*:r',ms = 20)# yıldız noktalı kırmızı
plt.show()
#%%
plt.figure(5)
plt.plot(ypoints,linestyle = 'dashed',color='red', marker = 'o', ms = 20, mec = '#000000', mfc = '#4CAF50')#mec dış mfc iç marker için
plt.figure(6)
#lw linewidth aynı
plt.plot(ypoints,ls = 'dashed',c='red',lw='10', marker = 'o', ms = 20, mec = '#000000', mfc = '#4CAF50')#mec dış mfc iç marker için
plt.show()


y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.figure(7)
plt.plot(y1)
plt.plot(y2)

plt.show()
#%%iki grafiği bir plotta gösterme
plt.figure(8)

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
#%%Label belirleme
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.figure(9)
plt.plot(x, y)
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1,loc='left')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.grid()
#plt.grid(axis = 'x') x yönünde böler
#plt.grid(axis='y') y yönünde böler
#plt.grid(color = 'green', linestyle = '--', linewidth = 0.5) gridi özelleştirir
plt.show()

#%%subplot
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])


plt.figure(10)
plt.subplot(2, 2, 1)#1 satır 2 sütun ve 1. si için
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 2)#2 satır 2 sütun ve 2. si için
plt.plot(x,y)
plt.subplot(2, 2, 4)#1 satır 2 sütun ve 2. si için
plt.plot(x,y)
plt.show()

plt.figure(11)
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
#2 satır 1 sütun ve 1.si
plt.title("3,8,1,10")
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)#2 ssatır 1 sütun ve 2.si
plt.title("deneme")
plt.plot(x,y)

plt.suptitle("grafik ana başlık")
plt.show()
#%%scatter plot

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)
plt.show()

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()

#%%herbir noktayı ayrı renkle göstermek

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()

#%%color map kullanımı
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')# burada color bar viridis
#color barlar bu linkte https://www.w3schools.com/python/matplotlib_scatter.asp

plt.colorbar()# bunu kullanırsanız colorbar çıkar

plt.show()
#%%size ve renk ve alpha belirleme

x = np.random.randint(100, size=(100))#0 ile 100 arasında 100 adet sayı
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()
#%%bar plot
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)

#plt.barh(x,y) horizontal bar oluşturur
#plt.bar(x, y, color = "red") kırmızı bar oluşturur
#plt.bar(x, y, width = 0.5) barın genişliğini belirtebiliriz
#plt.barh(x, y, height = 0.1) bar h da barın yüksekliği
plt.show()

#%%histogram bar
#histogram bir seride değerlerin adedini yani dağılımının grafiğidir
#normal dağılım üretmek için (çan eğrisi düşünülebilir ortlalaması 170
#standart sapması 10 olan ve 100000 e karşılık 100000 adet değer üreten bir normal
#dağılım seirisi aşağıda üretilmiştir) yaklaşık 3 ss de sağda sıfır 3 ssde solda sıfır
#görülür örneğin dünyadaki insanların boylarının olasılık dağılımı

import numpy as np
import matplotlib.pyplot as plt 
x = np.random.normal(170, 10, 100000)

plt.hist(x, 100)
plt.show()
#%%piechart grafik
y = np.array([35, 25, 25, 15])
plt.subplot(3, 3, 1)
plt.pie(y)
plt.show() 

plt.subplot(3, 3, 2)
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 



plt.subplot(3, 3, 3)
plt.title("derecesi 90dan başla")
plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 


plt.subplot(3, 3, 4)
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

plt.subplot(3,3,5)
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 


plt.subplot(3,3,6)
plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 

plt.subplot(3,3,7)
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 

plt.subplot(3,3,8)
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 




#%%
import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)

print(df.Species.unique())#benzersiz veri

print(df.info())

print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())

# %%
import matplotlib.pyplot as plt


df1 = df.drop(["Id"],axis=1)
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label= "virginica")
plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()


df1.plot(grid=True,alpha= 0.9)
plt.show()


#%% scatter plot

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

# %% histogram

plt.hist(setosa.PetalLengthCm,bins= 50)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

# %% bar plot

import numpy as np

#x = np.array([1,2,3,4,5,6,7])
#
#y = x*2+5
#
#plt.bar(x,y)
#plt.title("bar plot")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()


x = np.array([1,2,3,4,5,6,7])
a = ["turkey","usa","a","b","v","d","s"]
y = x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %% subplots

df1.plot(grid=True,alpha= 0.9,subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.ylabel("versicolor -PetalLengthCm")
plt.show()



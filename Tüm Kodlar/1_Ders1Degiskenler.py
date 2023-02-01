# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:05:38 2022

@author: SerdarKR
"""
#%%
#Değişkenler ()sayılar
var1=1
print(var1)
var2=10.0
print(type(var2))
var3=var1+var2

#%%
#değişkenler string
varstr1="Merhaba Arkadaşlar"
varstr2="İyi dersler"
print(varstr1+" "+varstr2)
uzunluk = len(varstr1)
print(uzunluk)
buyukharf=(varstr1+varstr2).upper()
print(buyukharf)
#%%
#degisken=varstr1+var1
#%%
print(type(buyukharf))
varfloat=10.55
varint1=20
varsonuc=int(varfloat)+varint1
varsonuc1=varfloat+varint1
varstrint="255"
varsonuc2=int(varstrint)+5
varstrint2="A"
#varsonuc3=int(varstrint2)+5
int1=5
int2=6
varsonuc4=str(int1)+str(int2)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
#%%
#global ve local degiskenler
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc1():
  global x1
  x1 = "fantastic"

myfunc1()

print("Python is " + x1)

x2 = "awesome"

def myfunc2():
  global x2
  x2 = "fantastic"

myfunc2()

print("Python is " + x2)

#%%
z = -87.7e10
print(z)
print(type(z))
import random

print(random.randrange(1, 10))
#%%
#string işlemleri
str10="Ankara"
print(str10[0])
print(len(str10))
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

txt = "The best things in life are free!"
print("free" in txt)
vardeger="free" in txt

txt1 = "The best things in life are free!"
print("expensive" not in txt1)
#%%string slicing
b = "Hello, World!"
print(b[2:5])

b1=b[5:]
b2=b[:6]
b3=b[:-1]
b4=b[-5:-1]

a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("l", "n",2))

a = "Hello, World!"
x1=a.split(",")
print(type(x1))
print(x1)
print(x1[0])
print(len(x1))
print("Hello" in x1) 
print("Hello" in x1[1]) 
print(type(x1[0]))
print(x1[0] in x1[1])
print(len(x1[0])==len(x1[1]))

#%%string formatlama
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)






























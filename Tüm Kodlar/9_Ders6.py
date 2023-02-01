# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:24:23 2022

@author: SerdarKR
"""

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar,"\n")
print(type(myvar)) 
print(myvar[0])

#label oluşturma
myvar1 = pd.Series(a, index = ["x", "y", "z"])
print(myvar1)

print(myvar1.index)
for each in myvar1.index:
    print(each)

print(myvar1.x,"\n")

print(myvar1["x"])
#labeled seri
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar2 = pd.Series(calories)
print("\n",myvar2)
#sadece day1 ve day 2 den seri oluşturma

myvar3 = pd.Series(calories, index = ["day1", "day2"])
print("\n",myvar3)


df1=pd.read_csv('data.csv')
import math as mt

import bosluktemizle as bt


data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3]}

df2=pd.DataFrame(data)

df3 = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])    

df3=df3.drop(df3.index[2])
df4=df3.drop(['Cochice', 'Pima'])
df5=df3.drop('reports', axis=1)

df6=df3[df3.name != 'Molly']

df7=df3.drop(df3.index[[1,2]])

df=pd.DataFrame(data)

df.drop(["name"],axis=1,inplace=True)

dfyear=pd.DataFrame(df["year"])

dfyear1=df[["year"]].copy()

dfyear2=df[["year"]]

#%%

dforjinal1 = pd.read_csv('data.csv')

dforjinal = pd.read_csv('data.csv')

print(dforjinal.iloc[17,3],"nan olması gerek")
print(dforjinal.loc[27,"Calories"],"nan olması gerek")

for each in range(len(dforjinal)):
    print(each)

for each in dforjinal.index:
    print(each)
    
for each in dforjinal.columns:
    print(each)

if(mt.isnan(dforjinal.loc[27,"Calories"])):
    print('nan')

mt.isnan(dforjinal.loc[27,"Calories"])

dftemiz=bt.temizle('data.csv')

dftemiz.drop(dftemiz.index[2],inplace=True)

dftemiz = dftemiz.reset_index(drop=True)

print(dforjinal.describe())
print(dforjinal["Duration"].describe())
print(dforjinal["Duration"].describe()[0])
print(dforjinal["Duration"].mode())
print(dforjinal["Duration"].mode()[0])
print(dforjinal["Duration"].mean())
print(dforjinal["Duration"].max())
print(dforjinal["Duration"].min())
print(dforjinal["Duration"].median())
print(dforjinal["Duration"].dtype.name)
print(type(dforjinal["Duration"].dtype.name))
print(dforjinal)


for kolon in dforjinal.columns:
    mean=dforjinal[kolon].mean()
    print(kolon,"ortalaması: ",mean)
    for satir in dforjinal.index:
        print(dforjinal.loc[satir,kolon])


for each in dforjinal.index:
    print(each)

for kolon in dforjinal.columns:
    print(kolon)

#%%
import boslukdoldur as bd
import pandas as pd
dforg=pd.read_csv("data.csv")
dfort=bd.boslukdoldur("data.csv",1)
dfmod=bd.boslukdoldur("data.csv", 3)
dfmed=bd.boslukdoldur("data.csv", 2)







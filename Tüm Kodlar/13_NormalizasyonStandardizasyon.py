# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:56:44 2022

@author: SerdarKR
"""

import pandas as pd
import numpy as np
import normstandrt as ns

df= pd.read_csv("verilernormstandrt.csv")
df1=df.copy()
print(df)
print(df.info())
print(df.describe())
ns.minmaxnorm(df,["boy","kilo","yas"],[0,1])
df_aralik=ns.minmaxnorm(df1.copy(),["boy","kilo","yas"],[10,100])
print(df)


ns.zscorestandart(df1,["boy","kilo","yas"])
print(df1)
import matplotlib.pyplot as plt
plt.figure(0)
plt.hist(df["yas"])
plt.show() 

plt.figure(1)
plt.boxplot(df["yas"])
plt.show()

plt.figure(2)
plt.hist(df["yas"])
plt.show() 

plt.figure(3)
plt.boxplot(df1["yas"])
plt.show()
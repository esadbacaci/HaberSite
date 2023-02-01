# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 13:19:28 2022

@author: SerdarKR
"""

from sklearn import datasets 
iris = datasets.load_iris()
# x ler features ye ler targetlar olacak ve gözlem değerleri olacak
# samples gözlem sayıları ve fatures özellikler kaç tane olacak
# target ta ise samples olacak ve target fatures ise 1 olacak
print(type(iris))
print(iris.data)
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


df= pd.DataFrame(iris.data)

print(df.head())

df.columns=iris.feature_names
df["targets"]=iris.target

targetnames = []
targetnames=iris.target_names

X=df.drop("targets",axis=1)
Y=df["targets"]

from sklearn.preprocessing import MinMaxScaler 

 # X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
 # X_scaled = (X_std * (max - min)) + min
  
mm_scaler=MinMaxScaler(feature_range=(0,1))
Xminmax=pd.DataFrame(mm_scaler.fit_transform(X))
Xminmax.columns=iris.feature_names
print(mm_scaler.data_min_)
print(mm_scaler.data_max_)

from sklearn.preprocessing import MaxAbsScaler

mas_scaler=MaxAbsScaler()

Xmaxabs=pd.DataFrame(mas_scaler.fit_transform(X))
Xmaxabs.columns=iris.feature_names


from sklearn.preprocessing import StandardScaler

ss_scaler= StandardScaler()

Xssscaler=pd.DataFrame(ss_scaler.fit_transform(X))
Xssscaler.columns=iris.feature_names


from sklearn.preprocessing import Normalizer

nm= Normalizer()

Xnm=pd.DataFrame(nm.fit_transform(X))
Xnm.columns=iris.feature_names

from sklearn.preprocessing import OrdinalEncoder

boy=["Uzun","Kısa","Normal","Kısa"]
df_boy=pd.DataFrame(boy)
df_boy.columns=["Boylar"]
oencoder=OrdinalEncoder(categories=[["Uzun","Kısa","Normal"]])
Xencode=oencoder.fit_transform(df_boy.Boylar.values.reshape(-1,1))
print(oencoder.categories_)


boyetiketleri={"Uzun":5,"Kısa":6,"Normal":7}
yenidfboylar=df_boy.Boylar.apply(lambda x:boyetiketleri[x])


##one hot encodings

from sklearn.preprocessing import OneHotEncoder

oencoder= OneHotEncoder()

sacrenkleri=["Sarı","Siyah","Beyaz","Sarı","Kahverengi"]
df_sac=pd.DataFrame(sacrenkleri)
df_sac.columns=["SacRenkleri"]
sacrenklerioe=pd.DataFrame(oencoder.fit_transform(df_sac).toarray())
sacrenklerioe.columns=["Beyaz","Kahverengi","Sarı","Siyah"]
sacrenklerioe.columns=oencoder.categories_

#sciitlearn ile eksik veri analizi

df.iloc[1,2]= np.nan
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(strategy='most_frequent')
df=pd.DataFrame(imputer.fit_transform(df))







#Scikitlearn ile veri önişleme
#nümerik verilernin ölçeklendirilmesi
#Ordinal verilerin yeniden kodlanması

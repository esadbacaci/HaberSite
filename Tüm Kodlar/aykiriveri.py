# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:25:08 2022

@author: SerdarKR
"""
import pandas as pd
import math as mt
import numpy as np
import statistics as st
from scipy import stats as stsc

def stratejibelirle(dfc,strateji):
    if strateji==1:
        sonuc=dfc.mean()
    elif strateji==2:
        sonuc=dfc.mode()[0]        
    else:
        sonuc=dfc.median()
    return sonuc

def aykiriveridoldur(df,strateji,yaklasim=0):
    for kolon in df.columns:
        if df[kolon].dtype!='O':
            y25=df[kolon].describe()[4]
            y75=df[kolon].describe()[6]
            ust=df[kolon].describe()[1]+df[kolon].describe()[2]
            alt=df[kolon].describe()[1]-df[kolon].describe()[2] 
            print(alt,"-",ust)
            sonuc=stratejibelirle(df[kolon],strateji)
            print(sonuc)
            if yaklasim==0:
                # print(yaklasim)
                # for satir in df[kolon].index:
                #     print(satir,df.loc[satir,kolon],df.loc[satir,kolon]<alt or df.loc[satir,kolon]>ust)
                #     if (df.loc[satir,kolon]<alt or df.loc[satir,kolon]>ust):
                #         df.loc[satir,kolon]=sonuc
                print(yaklasim)
                for satir in df[kolon].index:
                    if df.loc[satir,kolon]<y25 or df.loc[satir,kolon]>y75:
                        df.loc[satir,kolon]=sonuc
                        
            else:
                print(yaklasim)
                for satir in df[kolon].index:
                    if df.loc[satir,kolon]<alt or df.loc[satir,kolon]>ust:
                        df.loc[satir,kolon]=sonuc
                
    return df

       
           
    
def aykiriveridoldur1(df,strateji):
    for kolon in df.columns:
        if df[kolon].dtype!='O':
            q1=df[kolon].quantile(0.25)
            q3=df[kolon].quantile(0.75)
            iqr=q3-q1
            ust=q3+(1.5*iqr)
            alt=q1-(1.5*iqr)
            print(alt,"-",ust)
            sonuc=stratejibelirle(df[kolon],strateji)
            print(sonuc)           
            for satir in df[kolon].index:
                if df.loc[satir,kolon]<alt or df.loc[satir,kolon]>ust:
                    df.loc[satir,kolon]=sonuc
                
    return df

def aykiriveridoldur2(df,strateji):
    for kolon in df.columns:
        if df[kolon].dtype!='O':
            ortalama=df[kolon].mean()
            std=st.stdev(df[kolon])
            ust=ortalama+(1.96*std)
            alt=ortalama-(1.96*std)
            sonuc=stratejibelirle(df[kolon],strateji)
            print(sonuc)
            print("alt:",alt,"ust",ust,"sonuc:",sonuc)
            for satir in df[kolon].index:
                if df.loc[satir,kolon]<alt or df.loc[satir,kolon]>ust:
                    df.loc[satir,kolon]=sonuc
                
    return df

def aykiriveridoldur3(df,kolonlar,strateji,uzaklik=1.5):
    for kolon in kolonlar:
        print(kolon)
        if df[kolon].dtype != 'O':
            zscore=abs(stsc.zscore(df[kolon]))
            sonuc=stratejibelirle(df[kolon],strateji)
            df[kolon]=[sonuc if zscore[each]>uzaklik else df.loc[each,kolon] for each in df[kolon].index]
            #sdf=df.reset_index()
            #aşağıdaki gibi de olabilir             
            # for satir in df[kolon].index:
            #     if zscore[satir]>1.5:
            #         df.loc[satir,kolon]=sonuc
                
    return df    
    
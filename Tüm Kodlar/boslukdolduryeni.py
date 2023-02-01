# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:03:58 2022

@author: SerdarKR
"""

import math as mt
import pandas as pd

def boslukdoldurdf(df,strateji=1):
    """
    Parameters
    ----------
    dosyaadi : verilen dosya adınoku ve boş hücreleri olan satırları 
    parametre 1 ortalama
    parametre 2 median
    parametre 3 mode ile değiştirir    

    Returns 
    -------
    dataframe
             
               
        """
             
    dfdeneme = df
        
    for each in dfdeneme.columns:
        if dfdeneme[each].dtype == 'O':
           mode=dfdeneme[each].mode()
           dfdeneme[each].fillna(mode[0],inplace=True)
        else:
            ort = dfdeneme[each].mean()#calories ortalamasını alır
            medi=dfdeneme[each].median()#en ortadaki değer şayet çif ise ortadaki ikisinin ortalaması
            mode=dfdeneme[each].mode()
            if strateji==1:
                dfdeneme[each].fillna(ort,inplace=True)
            elif strateji==2:
                dfdeneme[each].fillna(medi,inplace=True)
            elif strateji==3:
                dfdeneme[each].fillna(mode[0],inplace=True)
          
    return dfdeneme  

def boslukdoldur(dosyaadi,strateji=1):
    """
    Parameters
    ----------
    dosyaadi : verilen dosya adınoku ve boş hücreleri olan satırları 
    parametre 1 ortalama
    parametre 2 median
    parametre 3 mode ile değiştirir    

    Returns 
    -------
    dataframe
             
               
        """
             
    dfdeneme = pd.read_csv(dosyaadi)   
        
    for each in dfdeneme.columns:
        if dfdeneme[each].dtype == 'O':
           mode=dfdeneme[each].mode()
           dfdeneme[each].fillna(mode[0],inplace=True)
        else:
            ort = dfdeneme[each].mean()#calories ortalamasını alır
            medi=dfdeneme[each].median()#en ortadaki değer şayet çif ise ortadaki ikisinin ortalaması
            mode=dfdeneme[each].mode()
            if strateji==1:
                dfdeneme[each].fillna(ort,inplace=True)
            elif strateji==2:
                dfdeneme[each].fillna(medi,inplace=True)
            elif strateji==3:
                dfdeneme[each].fillna(mode[0],inplace=True)
          
    return dfdeneme  
     
def boslukdoldur2(dosyaadi,strateji):
     
    """
    Açıklama:
    Veri Kolonu string ise mode'u alınır'
    Parameters
    ----------
    dosyaadi : verilen dosya adınoku ve boş hücreleri olan satırları 
    parametre 1 ortalama
    parametre 2 median
    parametre 3 mode ile değiştirir    

    Returns 
    -------               
        """
    dforjinal=pd.read_csv(dosyaadi)   
    
    for kolon in dforjinal.columns:
        if dforjinal[kolon].dtype == 'O':
            yerine=dforjinal[kolon].mode()[0]
            print(kolon,"mode'u alındı': ",yerine)
            for satir in dforjinal.index:
                if mt.isnan(dforjinal.loc[satir,kolon]):
                    dforjinal.loc[satir,kolon]=yerine
        else:
            yerine=[dforjinal[kolon].mean() if strateji==1 else dforjinal[kolon].median() if strateji==2 else dforjinal[kolon].mode()[0]]
            print(kolon,"strateji: ",yerine)
            for satir in dforjinal.index:
                if mt.isnan(dforjinal.loc[satir,kolon]):
                    dforjinal.loc[satir,kolon]=yerine
                    
    return dforjinal

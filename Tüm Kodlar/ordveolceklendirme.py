# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 13:17:00 2022

@author: SerdarKR
"""

def ordinalveri(df,kolon,sozluk):
    for x,y in sozluk.items():
        df[kolon]=[y if each==x else each for each in df[kolon] ]
    return df


def ordinalveri2(df,kolon,sozluk):
    df[kolon]=df[kolon].replace(sozluk)
    return df
    
    

      
def kesikli(df,kolon,sozluk,tip):    
    for x,y in sozluk.items():
        for each in df[kolon].index:
            try:
                if df[kolon][each]<y:
                    df[kolon][each]=x
                else: pass
            except:
                pass
    df[kolon]=df[kolon].astype(tip)
    return df

  
    
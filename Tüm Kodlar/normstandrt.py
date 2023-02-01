# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:01:04 2022

@author: SerdarKR
"""

import pandas as pd
import numpy as np


def minmaxnorm(df,kolonlar,aralik=[0,1]):
    """
    Parameters
    ----------
    df : TYPE
        DESCRIPTION.
    kolonlar : TYPE
        DESCRIPTION.
    aralik : aralik[0] min aralik [1] maks değerini içermelidir.
        DESCRIPTION. The default is [0,1].

    Returns
    -------
    df : TYPE
        DESCRIPTION.

    """
    for kolon in kolonlar:
        df[kolon]=df[kolon].astype(float)
        maxx=max(df[kolon])
        minx=min(df[kolon])
        print(kolon,":",maxx,minx)
        for satir in df[kolon].index:
            df[kolon][satir]=(float(df[kolon][satir])-float(minx))/(float(maxx)-float(minx))
        df[kolon]=df[kolon].apply(lambda x:(x*(aralik[1]-aralik[0]))+aralik[0])
    return df

def zscorestandart(df,kolonlar):
    for kolon in kolonlar:
        df[kolon]=df[kolon].astype(float)
        mean=df[kolon].mean()
        std=df[kolon].std()
        print(kolon,":",std,mean)
        for satir in df[kolon].index:
            df[kolon][satir]=(df[kolon][satir]-mean)/std
    return df
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:10:43 2022

@author: SerdarKR
"""

import pandas as pd
import math as mt
import numpy as np

def encoding(df,kolonlar):
    """
    Açıklama:
        Sadece string veriler üzerinde çalıştırınız.
    Parameters
    ----------
    df : Dataframe.
    kolonlar : işlem yapılacak kolonlar.

    Returns
    -------
    Dönüş boştur.
    Dataframe değişir çünkü referans aktarılır.

    """
    liste=[]
    for kolon in kolonlar:
        print(kolon)
        if df[kolon].dtype == 'O':
            u=len(df[kolon].unique())
            if u==2:
                df[kolon]=[1 if each==df[kolon].unique()[0] else 0 for each in df[kolon] ]
            else:
                for tekiller in df[kolon].unique():
                    print(tekiller)
                    liste.append(tekiller)
                    df[tekiller]=[1 if each==tekiller else 0 for each in df[kolon]]
                df.drop(kolon, axis='columns',inplace=True)
        
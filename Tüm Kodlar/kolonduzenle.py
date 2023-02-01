# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 23:17:13 2022

@author: SerdarKR
"""


def kolonduzenle(df,kolonlar,bicim):
    """
    Açıklama:
        Verilen kolonyada kolonların sayısal olması gerekliyse
        fakat hücrelerden birinde herhangi bir string varsa 
        sütunun data type'ı object olur bunu düzeltmek için
        bu fonksiyon yazılmıştır.
    Parameters
    ----------
    df : Dataframe
    kolonlar : Hangi Kolonlar düzenlenecekse.
    bicim : Kolonlar hangi formata çevrilecekse

    Returns
    -------
    df : dataframe'in yeni hali gönderilir.
    yollanan datframede değişir çünkü referans aktarımı gelir.

    """    
    for kolon in kolonlar:
        for index in df[kolon].index:
            if not df.loc[index,kolon].isnumeric():
                df.loc[index,kolon]=0
    df[kolon]=df[kolon].astype(bicim)
    return df
            
    
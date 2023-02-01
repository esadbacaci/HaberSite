# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:30:15 2022

@author: SerdarKR
"""

import pandas as pd
from scipy import stats as stsc

def stdnorm(df,kolonlar):
    for kolon in kolonlar:
        if df[kolon].dtype!='O':
            #vizeden sonra tamamlanacak
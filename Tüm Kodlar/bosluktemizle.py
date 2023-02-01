def temizle(dosyaadi):
     
    """
    Parameters
    ----------
    dosyaadi : verilen dosya adınoku ve boş hücreleri olan satırları temizler 
    ve dataframe geri döndürür
    

    Returns 
    -------
    dataframe

        """
   
    import pandas as pd
    dfdeneme = pd.read_csv(dosyaadi)
    try:
        liste=[]  
        for each in dfdeneme.columns:
            print(each,":te ki boşluk satırları")
            j=0
            x=len(dfdeneme)
               
            while j<x:
                try:
                    if pd.isna(dfdeneme.loc[j,each]): 
                        liste.append(j)
                        print(dfdeneme.index[j])
                    j=j+1             
                except:
                    print("hata oluştu")              
           
    except:
        print("An exception occurred")
    liste=set(liste)
    liste=list(liste)
    liste.sort()
    dfdeneme.drop(dfdeneme.index[liste],inplace=True)
    dfdeneme = dfdeneme.reset_index(drop=True)
    
    return dfdeneme

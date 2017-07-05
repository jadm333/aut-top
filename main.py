# -*- coding: utf-8 -*-
"""
@author: PEPE
"""
#%%
import os
os.chdir("C:/Users/PEPE/Documents/GitHub/aut-top")
import pandas as pd
import glob
import os
#%%
file_ ="Archivos_csv/JACrespo1.csv" # use your path
df =  pd.read_csv(file_,header=0, parse_dates=True, infer_datetime_format=True, index_col=0)
df['screen_name'] = os.path.splitext(os.path.basename(file_))[0]
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
del df['screen_name']
#%%

path ="Archivos_csv/" # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0,parse_dates=True,infer_datetime_format=True,index_col=1)
    
    list_.append(df)
df = pd.concat(list_)
del allFiles
del file_
del frame
del list_
del path

#%%
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
import preprocessor as p
import numpy as np
#%%
p.set_options(p.OPT.URL, p.OPT.EMOJI,p.OPT.RESERVED,p.OPT.SMILEY,p.OPT.NUMBER)
file_ ="Archivos_csv/JACrespo1.csv" # use your path
df =  pd.read_csv(file_,header=0, parse_dates=True, infer_datetime_format=True, index_col=0)
df['screen_name'] = os.path.splitext(os.path.basename(file_))[0]
del df['id_tweet']
del df['id_twitter']
del df['created_at']
del df['in_reply_to_user_id']
del df['in_reply_to_status_id']
del df['in_reply_to_screen_name']
del df['retweet_count']
del df['favorite_count']
del df['longitude']
del df['latitude']
del df['retweeted']
del df['creation_date']
del df['modification_date']
del df['RT_temp']
del df['is_retweeted']
df = df.loc[df['created_at_datetime'] > "2017-04-29"]
df['text'] = df['text'].apply(p.clean)
df['text'].replace('', np.nan, inplace=True)
df.dropna(subset=['text'], inplace=True)
#%% Leer archivos y hacer una primera limpieza

path ="Archivos_csv/"
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
p.set_options(p.OPT.URL, p.OPT.EMOJI,p.OPT.RESERVED,p.OPT.SMILEY,p.OPT.NUMBER)
for file_ in allFiles:
    df =  pd.read_csv(file_,header=0, parse_dates=True, infer_datetime_format=True, index_col=0)
    df['screen_name'] = os.path.splitext(os.path.basename(file_))[0]
    df = df.loc[df['RT_temp'] == 0]
    del df['id_tweet']
    del df['id_twitter']
    del df['created_at']
    del df['in_reply_to_user_id']
    del df['in_reply_to_status_id']
    del df['in_reply_to_screen_name']
    del df['retweet_count']
    del df['favorite_count']
    del df['longitude']
    del df['latitude']
    del df['retweeted']
    del df['creation_date']
    del df['modification_date']
    del df['RT_temp']
    del df['is_retweeted']
    df = df.loc[df['created_at_datetime'] > "2017-05-28"]
    df['text'] = df['text'].apply(p.clean)
    df['text'].replace('', np.nan, inplace=True)
    df.dropna(subset=['text'], inplace=True)
    df = df.drop_duplicates(subset = "text", keep='last')
    list_.append(df)
df = pd.concat(list_,ignore_index=True)
del allFiles
del file_
del frame
del list_
del path

#%%








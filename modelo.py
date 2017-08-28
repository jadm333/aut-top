# -*- coding: utf-8 -*-
"""
@author: PEPE

"""
#%%

#%% Paqueterias

import os
import pandas as pd
import glob
import os
import preprocessor as p
import numpy as np
import spacy

##Leer Archivos scv
def archivos_csv(path ="Archivos_csv/"):
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
        df = df.loc[df['created_at_datetime'] > "2017-08-03"]
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
    return df

def preprocesamiento(df):
    df['text'] = df['text'].str.replace('@','')
    df['text'] = df['text'].str.replace('#','')
    df['text'] = df['text'].str.replace('!','')
    df['text'] = df['text'].str.replace('¿','')
    df['text'] = df['text'].str.replace('?','')
    df['text'] = df['text'].str.replace("'",'')
    df['text'] = df['text'].str.replace('"','')
    df['text'] = df['text'].str.replace('%','')
    df['text'] = df['text'].str.replace('+','')
    df['text'] = df['text'].str.replace('=','')
    df['text'] = df['text'].str.replace('`','')
    df['text'] = df['text'].str.replace('~','')
    df['text'] = df['text'].str.replace('|','')
    df['text'] = df['text'].str.replace(';','')
    df['text'] = df['text'].str.replace('.','')

    nlp = spacy.load('es')

    nlp.vocab["y"].is_stop = True
    nlp.vocab["a"].is_stop = True
    nlp.vocab["ante"].is_stop = True
    nlp.vocab["a"].is_stop = True
    nlp.vocab["bajo"].is_stop = True
    nlp.vocab["con"].is_stop = True
    nlp.vocab["de"].is_stop = True
    nlp.vocab["desde"].is_stop = True
    nlp.vocab["durante"].is_stop = True
    nlp.vocab["en"].is_stop = True
    nlp.vocab["entre"].is_stop = True
    nlp.vocab["excepto"].is_stop = True
    nlp.vocab["hacia"].is_stop = True
    nlp.vocab["hasta"].is_stop = True
    nlp.vocab["mediante"].is_stop = True
    nlp.vocab["para"].is_stop = True
    nlp.vocab["por"].is_stop = True
    nlp.vocab["salvo"].is_stop = True
    nlp.vocab["según"].is_stop = True
    nlp.vocab["sin"].is_stop = True
    nlp.vocab["sobre"].is_stop = True
    nlp.vocab["tras"].is_stop = True
    nlp.vocab["y"].is_stop = True
    nlp.vocab["e"].is_stop = True
    nlp.vocab["ni"].is_stop = True
    nlp.vocab["o"].is_stop = True
    nlp.vocab["u"].is_stop = True
    nlp.vocab["que"].is_stop = True
    nlp.vocab["si"].is_stop = True
    nlp.vocab["como"].is_stop = True
    nlp.vocab["donde"].is_stop = True
    nlp.vocab["quien"].is_stop = True
    nlp.vocab["cual"].is_stop = True
    nlp.vocab["cuyo"].is_stop = True
    nlp.vocab["cuanto"].is_stop = True
    nlp.vocab["el"].is_stop = True
    nlp.vocab["lalos"].is_stop = True
    nlp.vocab["las"].is_stop = True

    
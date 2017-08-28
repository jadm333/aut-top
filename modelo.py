# -*- coding: utf-8 -*-
"""
@author: PEPE

"""
#%%

#%% Paqueterias

import os
import pandas as pd
import glob
import preprocessor as p
import numpy as np
import spacy
from gensim.corpora import Dictionary
from gensim.models import Phrases
# Leer Archivos scv

#%%
def archivos_csv(path="Archivos_csv/"):
    allFiles = glob.glob(path + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.RESERVED, p.OPT.SMILEY, p.OPT.NUMBER)
    for file_ in allFiles:
        df = pd.read_csv(file_, header=0, parse_dates=True, infer_datetime_format=True, index_col=0)
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
        df = df.drop_duplicates(subset="text", keep='last')
        list_.append(df)
    df = pd.concat(list_, ignore_index=True)
    del allFiles
    del file_
    del frame
    del list_
    del path
    return df

#%%
def preprocesamiento(df,max_freq=0.5):
    df['text'] = df['text'].str.replace('@', '')
    df['text'] = df['text'].str.replace('#', '')
    df['text'] = df['text'].str.replace('!', '')
    df['text'] = df['text'].str.replace('¿', '')
    df['text'] = df['text'].str.replace('?', '')
    df['text'] = df['text'].str.replace("'", '')
    df['text'] = df['text'].str.replace('"', '')
    df['text'] = df['text'].str.replace('%', '')
    df['text'] = df['text'].str.replace('+', '')
    df['text'] = df['text'].str.replace('=', '')
    df['text'] = df['text'].str.replace('`', '')
    df['text'] = df['text'].str.replace('~', '')
    df['text'] = df['text'].str.replace('|', '')
    df['text'] = df['text'].str.replace(';', '')
    df['text'] = df['text'].str.replace('.', '')
    df['text'] = df['text'].str.replace('á', '')
    df['text'] = df['text'].str.replace('à', '')
    df['text'] = df['text'].str.replace('é', '')
    df['text'] = df['text'].str.replace('.', '')
    df['text'] = df['text'].str.replace('‘', '')
    df['text'] = df['text'].str.replace('.', '')
    df['text'] = df['text'].str.replace('.', '')
    df['text'] = df['text'].str.replace('.', '')
    df['text'] = df['text'].str.replace('.', '')

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

    docs = list(df['text'])

    processed_docs = []
    for doc in nlp.pipe(docs, n_threads=4, batch_size=100):

        ents = doc.ents

        doc = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

        doc.extend([str(entity) for entity in ents if len(entity) > 1])

        processed_docs.append(doc)

    docs = processed_docs
    del processed_docs
    #BIGRAMAS
    

    bigram = Phrases(docs, min_count=20)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                docs[idx].append(token)

    #FILTRAR EXTREMOS
    
    dictionary = Dictionary(docs)
    min_wordcount = 2
    dictionary.filter_extremes(no_below=min_wordcount, no_above=max_freq)

    dictionary.filter_n_most_frequent()
    _ = dictionary[0]

    corpus = [dictionary.doc2bow(doc) for doc in docs]

    # Borrar tweets vacios y actualizar corpus

    id_borrar = [i for i in range(0,len(corpus)) if len(corpus[i]) == 0]
    df = df.drop(df.index[id_borrar])
    df = df.reset_index(drop=True)
    docs = list(df['text'])
    processed_docs = []
    for doc in nlp.pipe(docs, n_threads=4, batch_size=100):
        ents = doc.ents

        doc = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
        doc.extend([str(entity) for entity in ents if len(entity) > 1])
        processed_docs.append(doc)
    docs = processed_docs
    del processed_docs
    bigram = Phrases(docs, min_count=20)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                docs[idx].append(token)
    dictionary = Dictionary(docs)
    _ = dictionary[0]
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    #Crear author2doc
    author2doc = {}
    df.text.unique()
    for aut in df.screen_name.unique():
        author2doc[aut] = []
        
    for index, row in df.iterrows():
        author2doc[row['screen_name']].append(index)

    print('# de autores: %d' % len(author2doc))
    print('# tokens unicos: %d' % len(dictionary))
    print('# de documentos: %d' % len(corpus))

    return corpus, dictionary, author2doc
#%%
if __name__ == '__main__':
    df = archivos_csv()
    corpus, dictionary, author2doc = preprocesamiento(df)


#%%
df = archivos_csv()
corpus, dictionary, author2doc = preprocesamiento(df)







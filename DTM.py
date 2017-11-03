
#%% PAQUETERIAS
from gensim.models import ldaseqmodel
from gensim.corpora import Dictionary, bleicorpus
import numpy
from gensim.matutils import hellinger

#%%Cargar datos

# loading our corpus and dictionary
try:
    dictionary = Dictionary.load('datasets/news_dictionary')
except FileNotFoundError as e:
    raise ValueError("SKIP: Please download the Corpus/news_dictionary dataset.")
corpus = bleicorpus.BleiCorpus('datasets/news_corpus')
# it's very important that your corpus is saved in order of your time-slices!

time_slice = [438, 430, 456]



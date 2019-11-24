# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:29:52 2019

@author: Kanika Chopra
"""
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nlp import get_pos

def jaccard(str1, str2):
    '''
    '''
    a = set(str1.split())
    b = set(str2.split())
    
    c = a.intersection(b)
    
    return float(len(c))/(len(a) + len(b) - len(c))

def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()
    

def cosine(*strs):

    vectors = [vec for vec in get_vectors(*strs)]
    return cosine_similarity(vectors)
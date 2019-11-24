# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:23:38 2019

@author: Kanika Chopra
"""

import spacy
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer 


import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

def get_pos(word):
    ''' 
    We take the position tag of each of the words and then abbreviate it as:
        ADJ -> J
        NOUN -> N
        VERB -> V
        ADVERB -> R
    
    Args:
        word (str): the word that we need the part of speech for 
    
    Returns: 
    
    @author: Kanika Chopra
    '''
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {'J': wordnet.ADJ,
                'N': wordnet.NOUN,
                'V': wordnet.VERB,
                'R': wordnet.ADV}
    
    return tag_dict.get(tag, wordnet.NOUN)

def spacy_lemmatize(sentence):
    '''
    Given a sentence, this will use spaCy's lemmatization tools to lemmatize
    the words in the sentence and tokenize them 
    
    Args: 
        sentence (str): The sentence to be tokenized and lemmatized 
    Returns:
        A list of words in the sentence after lemmatization 
    
    '''
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    doc = nlp(sentence)
    
    return [token.lemma_ for token in doc]

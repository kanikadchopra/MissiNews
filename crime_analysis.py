# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:58:53 2019

@author: Kanika Chopra
"""

import pandas as pd

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

from collections import Counter

import contractions
from string import punctuation

from nlp import *

def crime_analysis(year):
    '''
    Reads in the CSV data for the Tweets and will only keep the data that fits
    within the month and year range. It will conduct a crime analysis to show 
    the number of shootings, stabbings, assaults and robberies per month
    and to show the overall frequency as an Interactive Plot.
    
    Args:
        year (int): The year that you want to use for the data 
    
    Returns:
        Plot.ly Interactive Plot with subplots showing the overall crime 
        analysis for the year.
        
    '''
    # Read in the data
    df = pd.read_csv('MissiNewsRoom_tweets.csv')

    # Clean up the columns and create sections for the Year, Month
    df.drop(columns=['Unnamed: 0', 'id'], inplace=True)
    df.columns = ['Timestamp', 'Tweet']
    
    # Break the Date apart into Date and Time 
    df['Time'] = df['Timestamp'].apply(lambda x: x[10:])
    df['Date'] = df['Timestamp'].apply(lambda x: x[:10])
    df['Month'] = df['Date'].apply(lambda x: x[5:7])
    df['Year'] = df['Date'].apply(lambda x: x[:4])
    
    # Reorder the columns
    df = df[['Date', 'Year', 'Month', 'Time', 'Tweet']]
    
    # Only use the dates that we need 
    df = df[df['Year'] == str(year)]
    
    # We need to separate the link from the tweet
    df['Link'] = df['Tweet'].apply(lambda x: 'http' + x.split('http')[1] if 'http' in x else '')
    df['Tweet'] = df['Tweet'].apply(lambda x: x.split('http')[0] if 'http' in x else x)
    
    # Break apart all contractions (except name possession e.g. Sarah's)
    df['Tweet'] = df['Tweet'].apply(lambda x: contractions.fix(x))
    
    df['tokens'] = nlp_cleanse(df['Tweet'])
    df['Cleaned_Tweet'] = df['tokens'].apply(lambda x: ' '.join(x))
    
    return df
    
def nlp_cleanse(ser):
    '''
    nlp_cleanse takes a pandas Series that has strings as the values and will
    tokenize, lemmatize and remove stop words for the string. It will return
    a series where the values are a list of strings after this process.
    
    Args: 
        ser (Series): pandas Series with the values being strings for nlp analysis
        
    Returns: 
        Series where the values are list of strings after tokenization, 
        lemmatization and cleaning
        
    '''
    
    # Initialize the tokenizer so that it doesn't include punctuation 
    tokenizer = RegexpTokenizer(r'\w+')

    ser = ser.apply(lambda x: x.lower())
    
    # Tokenization
    ser = [tokenizer.tokenize(x) for x in ser]
    
    # Remove stopwords 
    stop_words = set(stopwords.words('english'))
    
    # Make ser into a series again
    ser = pd.Series(ser)
    
    ser = ser.apply(lambda x: [word for word in x if word not in stop_words])
    
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer() 
    
    ser = ser.apply(lambda x: [lemmatizer.lemmatize(word, get_pos(word)) for word in x])
    
    return ser
    
    
def crime_topics(month, df):
    ''' 
    Crime topics takes a month and a DataFrame with yearly data and will sort 
    out the data to only analyze the frequency of crimes from the list of crime
    words for that month in the given year.
    
    Args: 
        month (str): Month for analysis, must be in the form of '01' for January,
                    '11' for November, etc.
        df (DataFrame): The DataFrame with all the information about the crimes
                        with the dates for analysis
                        
    Returns:
        Returns a DataFrame where the crime words mentioned are added as another column into
        the DataFrame 
        
    '''
    
    # Set the crime_words that we are focusing on first
    crime_words = ['police', 'shoot',  'stab', 'robs', 'robbery', 'assault']   
    
    # Subset the data to only that month 
    df = df[df['Month']  == month]
    
    month_crime = pd.DataFrame(columns=df.columns)
    
    for word in crime_words:
        subset = df[df['Cleaned_Tweet'].str.contains(word)]
        subset['word'] = word
        month_crime = month_crime.append(subset)
        
    month_crime.reset_index(inplace=True,drop=True)
    
    return month_crime

def overall_crime_analysis(year):
    ''' 
    Takes a year and will return an overall analysis of the frequency of the 
    crimes related to shootings, stabbings, robberies, and assaults in the 
    year
    
    Args:
        year (int): Year for analysis
    
    Returns:
        DataFrame with the crime words as the columns and the rows are each of 
        the months in the year with the frequency being the values
    '''
            
    df = crime_analysis(year)
    
    # Get the list of months to use in the crime_topics function
    months = []
    for i in range(1,13):
        num = str(i)
        if len(num)!=2:
            num = '0' + num 
        months.append(num)    
        
    # Create the year crimes dataframe
    yr_crimes = pd.DataFrame(columns=['police', 'shoot', 'stab', 'robbery', 'assault'])

    # Append all the monthly analysis to this dataframe
    for month in months:
        data_i = crime_topics(month, df)['word'].value_counts()
        yr_crimes = yr_crimes.append(data_i)
       
    # Change the index to the month abbreviations
    yr_crimes.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug' , 'Sep', 'Oct', 'Nov', 'Dec']
    
    return yr_crimes
        
    
    
    
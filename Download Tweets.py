# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:59:44 2019

@author: RQ
"""

import tweepy
import csv
import pandas as pd 


#Twitter API credentials
consumer_key = '67wC5riTM5AAIIUCJIyW6ro82'
consumer_secret = 'vvIP8mFkmlBM81bAMI37OtUwDHUJwfXXNkTfyQnGn2NXv8PVEB'
access_token = '560674182-qEeArvmgeCAf6vSZxTZGyMyn8v94FfnCBBADv6pu'
access_token_secret = 'DHkQc3r4KWOPb8xeS2C8fMkfycq5DgwKzVn4MrrydcVTF'

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode='extended')
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before {oldest}".format(oldest=oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest, tweet_mode='extended')
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...{number} tweets downloaded so far".format(number= len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    
    # Create a DataFrame
    df = pd.DataFrame(outtweets)
    cols = ['id', 'Date', 'Tweet']

    
    df[2] = df[2].apply(lambda x: x.decode('utf-8'))
    
    df.columns = cols
    
    # Need to split by https:// and then itll be id, date, tweet, and links 
    # how do i get the location?? 
    
    tweet.decode('utf-8')
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass

# >>> b"abcde".decode("utf-8") 

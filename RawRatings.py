#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Use TextBlob to analyze tweets about movies to generate sentiment scores.
A simple rating system for movies. 
Example queries:
"Knives Out" 0.251
"Star Wars Rise Skywalker" 0.218
"Frozen 2" 0.191
"Jumanji Next Level" 0.187
"Richard Jewell" 0.243
"Cats movie" 0.059
"Ford Ferrari" 0.233
"Beautiful Day Neighborhood" 0.628 (due to "Beautiful" being counted)
"Parasite movie" 0.389

"""
import json

#open json file of tweets
with open('tweets.json','r') as f:
    tweet_data = json.load(f)

# extract just the text of each tweet into a list
tweet_text = []
for i,_ in enumerate(tweet_data):
    try:
        tweet_text.append(tweet_data[i]['extended_tweet']['full_text'])
    except:
        try:
            tweet_text.append(tweet_data[i]['text'])
        except:
            print('not a good tweet')            

# convert each tweet into a TextBlob and use TextBlob to do a sentiment score
from textblob import TextBlob

tweet_blob = [TextBlob(tweet) for tweet in tweet_text]
tweet_scores = [tweet.sentiment.polarity for tweet in tweet_blob]

#make tuples of tweets and their scores
tweets_and_scores = zip(tweet_text,tweet_scores)
tweets_and_scores = list(set(tweets_and_scores))
tweets_and_scores = [(text,score) for text,score in tweets_and_scores if score != 0.0]

# sort the tweets by score for manual inspection
sorted_tweets = sorted(tweets_and_scores,key=lambda x: float(x[1]))

# give the net rating
_,just_scores = zip(*tweets_and_scores)
print(sum(just_scores)/len(just_scores))

    
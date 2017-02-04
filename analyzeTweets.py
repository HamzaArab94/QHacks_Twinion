# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 02:57:22 2017

@author: Family
"""

import json
import pandas as pd
#import matplotlib.pyplot as plt
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
    
def add_field(df, field):
    df[field] = tweets[field].apply(lambda tweet: word_in_text(field, tweet))

tweets_data_path = 'facebooktweets.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
    
    
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)


#tweets['stock'] = tweets['text'].apply(lambda tweet: word_in_text('stocks', tweet))
#tweets['trade'] = tweets['text'].apply(lambda tweet: word_in_text('trade', tweet))
tweets['facebook'] = tweets['text'].apply(lambda tweet: word_in_text('facebook', tweet))


    
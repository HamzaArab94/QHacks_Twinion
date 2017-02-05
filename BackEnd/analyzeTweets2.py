import json
import pandas as pd
import re
import string
import numpy as np
import indicoio



def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def filterTweets(inputFile, keyword, numTweets):
    tweets_data = []
    #tweets_file = open(inputFile, "r")
    with open(inputFile) as f:
        tweets_data = json.load(f)
        
    
    #tweets_data = [tweet for tweet in tweets_data if 'lang' in tweet]
    tweets = pd.DataFrame()
    
    tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
    
    #tweets[keyword] = tweets['text'].apply(lambda tweet: word_in_text(keyword, tweet))
    result = []  
    count = 0
    
    for tweet in tweets['text']:
        if word_in_text(keyword, tweet):
            result.append(tweet)
            count += 1
            
        if (count >= numTweets):
            break
    #tweets = tweets[tweets[keyword] == True]
    # tweets['trade'] = tweets['text'].apply(lambda tweet: word_in_text('trade', tweet))
    # tweets['facebook'] = tweets['text'].apply(lambda tweet: word_in_text('facebook', tweet))
    for tweet in result:
        #Gets rid of unreadable characters
        tweet = ''.join(filter(lambda x: x in string.printable, tweet))
    
    return result


def NLPOutput(tweetsList):
    indicoio.config.api_key = '6d8a020272686a662976e9afdbf98b82'
    
    #Uses indicoio
    review = indicoio.analyze_text(tweetsList, apis=['sentiment', 'twitter_engagement'])
    
    sentimentArray = np.array(review['sentiment'])
    for i in range(len(sentimentArray)):
        sentimentArray[i] = (sentimentArray[i] - 0.5) * 100
        
    engagementArray = np.array(review['twitter_engagement'])
    
    productArray = sentimentArray * engagementArray

    productScore = 0    
    
    for i in productArray:
        productScore += i
    
    """if productScore < 0:
        print("People have a negative opinion towards this")
    elif productScore >= 0:
        print("People feel okay about this topic")
    elif productScore > 5:
        print("The people feel great about topic.")"""
    return productScore
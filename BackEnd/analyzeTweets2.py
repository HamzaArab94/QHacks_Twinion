import json
import pandas as pd
import re
import string
import numpy as np
import indicoio

#Check if a word is in a text passage
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

#Filter tweets based on a key word
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

# Analysis of Liking/Disliking Topic with Engagement
#Determine whether the public likes or dislikes the topic
def sentimentalOutput(tweetsList):
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
    
    return productScore

#Analysis of Political Views
#Determine the tweets with the most leaning political view
def politicalOutput(tweetsList):
    indicoio.config.api_key = '6d8a020272686a662976e9afdbf98b82'

    politics = indicoio.political(tweetsList)

    Array = np.array(politics)
    litar_count = 0
    lib_count = 0
    con_count = 0
    green_count = 0

    for di in Array:
        litar_count += di['Libertarian']
        lib_count += di['Liberal']
        con_count += di['Conservative']
        green_count += di['Green']
        
    counts = (litar_count, lib_count, con_count, green_count)
    if (litar_count == max(counts)):
        return "Libertarian"
    elif (lib_count == max(counts)):
        return "Liberal"
    elif con_count == max(counts):
        return "Conservative"
    else:
        return "Green"
    
# Analysis of Personalities
#Determine most dominating personality relating to the topic
def PersonalityOutput(tweetsList):
    indicoio.config.api_key = '6d8a020272686a662976e9afdbf98b82'

    personality = indicoio.personality(tweetsList)

    personalityArray = np.array(personality)
    openness_count = 0
    cons_count = 0
    extra_count = 0
    agree_count = 0

    for do in personalityArray:
        openness_count += do['openness']
        cons_count += do['conscientiousness']
        extra_count += do['extraversion']
        agree_count += do['agreeableness']
        
    counts = (openness_count, cons_count, extra_count, agree_count)
    if (openness_count == max(counts)):
        return "Openness"
    elif (cons_count == max(counts)):
        return "Conscientiouesness"
    elif extra_count == max(counts):
        return "Extroversion"
    else:
        return "Agreeableness"

# Analysis of Emotions
#Determine most prominent emotion relating to the topic
def emotionalOutput(tweetsList):
    indicoio.config.api_key = '6d8a020272686a662976e9afdbf98b82'

    emotions = indicoio.emotion(tweetsList)

    emotionalArray = np.array(emotions)
    anger_count = 0
    joy_count = 0
    fear_count = 0
    sad_count = 0
    surprise_count = 0

    for de in emotionalArray:
        anger_count += de['anger']
        joy_count += de['joy']
        fear_count += de['fear']
        sad_count += de['sadness']
        surprise_count += de['surprise']

    counts = (anger_count, joy_count, fear_count, sad_count, surprise_count)
    
    if (anger_count == max(counts)):
        return "Anger"
    elif (joy_count == max(counts)):
        return "Joy"
    elif fear_count == max(counts):
        return "Fear"
    elif sad_count == max(counts):
        return "Sadness"
    else:
        return "Shock"
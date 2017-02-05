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


# Analysis of Liking/Disliking Topic with Engagement
#Determine whether the public likes or dislikes the topic
def SentimentalOutput(tweetsList):
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

#Analysis of Political Views
#Determine the tweets with the most leaning political view
def PoliticalOutput(tweetsList):
    indicoio.config.api_key = '6d8a020272686a662976e9afdbf98b82'

    politics = indicoio.political(tweetsList)

    Array = np.array(politics)
    count = len(Array)
    litar_count = 0
    lib_count = 0
    con_count = 0
    green_count = 0

    for di in Array:
        litar_count += di['Libertarian']
        lib_count += di['Liberal']
        con_count += di['Conservative']
        green_count += di['Green']
    lst = []
    Libraterians = ((litar_count / count) * 100)
    lst.append(Libraterians)
    Liberals = ((lib_count / count) * 100)
    lst.append(Liberals)
    Conservatives = ((con_count / count) * 100)
    lst.append(Conservatives)
    Greens = ((green_count / count) * 100)
    lst.append(Greens)

    politicalScore = 0
    for i in lst:
        if politicalScore < i:
            politicalScore = i
    return politicalScore

# Analysis of Personalities
#Determine most dominating personality relating to the topic
def PersonalityOutput(tweetsList):
    indicoio.config.api_key = '6d8a020272686a662976e9afdbf98b82'

    personality = indicoio.personality(tweetsList)

    personalityArray = np.array(personality)
    personality_count = len(personalityArray)
    openness_count = 0
    cons_count = 0
    extra_count = 0
    agree_count = 0

    for do in personalityArray:
        openness_count += do['openness']
        cons_count += do['conscientiousness']
        extra_count += do['extraversion']
        agree_count += do['agreeableness']
    personalitylst = []
    Openness = ((openness_count / personality_count) * 100)
    personalitylst.append(Openness)
    Concientiousness = ((cons_count / personality_count) * 100)
    personalitylst.append(Concientiousness)
    Extraversion = ((extra_count / personality_count) * 100)
    personalitylst.append(Extraversion)
    Agreeableness = ((agree_count / personality_count) * 100)
    personalitylst.append(Agreeableness)

    personalityScore = 0
    for i in personalitylst:
        if personalityScore < i:
            personalityScore = i
    return personalityScore

# Analysis of Emotions
#Determine most prominent emotion relating to the topic
def EmotionalOutput(tweetsList):
    indicoio.config.api_key = '6d8a020272686a662976e9afdbf98b82'

    emotions = indicoio.emotion(tweetsList)

    emotionalArray = np.array(emotions)
    emo_count = len(emotionalArray)
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

    emotionallst = []
    Anger = ((anger_count / emo_count) * 100)
    emotionallst.append(Anger)
    Joy = ((joy_count / emo_count) * 100)
    emotionallst.append(Joy)
    Fear = ((fear_count / emo_count) * 100)
    emotionallst.append(Fear)
    Sad = ((sad_count / emo_count) * 100)
    emotionallst.append(Sad)
    Surprise = ((surprise_count / emo_count) * 100)
    emotionallst.append(Surprise)
    
    emotionalScore = 0
    for i in emotionallst:
        if emotionalScore < i:
            emotionalScore = i
    return emotionalScore

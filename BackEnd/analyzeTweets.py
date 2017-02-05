"""
"""
import indicoio
import json
import pandas as pd
import re
import string
import time
import numpy as np


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


def add_field(df, field):
    df[field] = df[field].apply(lambda tweet: word_in_text(field, tweet))


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

tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))

tweets = tweets[tweets.lang == "en"]

for tweet in tweets['text']:
    tweet = ''.join(filter(lambda x: x in string.printable, tweet))




indicoio.config.api_key = '6d8a020272686a662976e9afdbf98b82'

tweetsList = tweets['text'].tolist()

start = time.time()

# NLP based on Sentiments
a= indicoio.sentiment(tweetsList)
print(a)


#Approval Rating of Companies based on Sentiments
# aggregate_score = 0
total = 0
for i in a:
    total += i
    # aggregate_score += i - 0.5
avg = total/len(a)


# print (aggregate_score)
approval_rating = avg * 100
print ("Approval Rating: " + str(approval_rating) + "%")
# if aggregate_score > 0:
    # print("Invest!")
# else:
   #  print("Dont Invest!")
end = time.time()

print (end - start)

start2 = time.time()

#Analysis of Sentiment and Engagement
review = indicoio.analyze_text(tweetsList, apis=['sentiment', 'twitter_engagement'])


sentimentArray = np.array(review['sentiment'])
for i in range(len(sentimentArray)):

    sentimentArray[i] = (sentimentArray[i] - 0.5) * 100
engagementArray = np.array(review['twitter_engagement'])

productArray = sentimentArray * engagementArray

aggregate_score = 0

for i in productArray:
    aggregate_score += i - 0.5

if aggregate_score > 0:
    print("The people feel good about topic.")
    if aggregate_score > 3:
        print("The topic has lots of engagement.")
else:
    print("The people feel bad about topic.")
    if aggregate_score > 3:
        print("The topic has lots of engagement.")


#Analysis of Political Views
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

print(((litar_count / count) * 100), ((lib_count / count) * 100), ((con_count / count) * 100), ((green_count / count) * 100))

# NLP based on Keywords
keywords= indicoio.keywords(tweetsList, top_n = 5, version=2)

# NLP based on Personality
personality= indicoio.personality(tweetsList)


personalityArray = np.array(personality)
personality_count = len(personalityArray)
open_count = 0
cons_count = 0
extra_count = 0
agree_count = 0


for do in personalityArray:
    open_count += do['openness']
    cons_count += do['conscientiousness']
    extra_count += do['extraversion']
    agree_count += do['agreeableness']

print(((open_count / personality_count) * 100), ((extra_count / personality_count) * 100), ((cons_count / personality_count) * 100), ((agree_count / personality_count) * 100))

#Analysis of Emotional Views
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


print(((anger_count / emo_count) * 100), ((joy_count / emo_count) * 100), ((fear_count / emo_count) * 100), ((sad_count / emo_count) * 100), ((surprise_count / emo_count) * 100))


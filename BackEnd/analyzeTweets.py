"""
"""
import indicoio
import json
import pandas as pd
import re
import string
import time

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def add_field(df, field):
    df[field] = df[field].apply(lambda tweet: word_in_text(field, tweet))


def filterTweets(inputFile, keyword):
    tweets_data = []
    tweets_file = open(inputfile, "r")
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
    tweets[keyword] = tweets['text'].apply(lambda tweet: word_in_text('stocks', tweet))
    tweets = tweets[tweets.keyword == True]
    # tweets['trade'] = tweets['text'].apply(lambda tweet: word_in_text('trade', tweet))
    # tweets['facebook'] = tweets['text'].apply(lambda tweet: word_in_text('facebook', tweet))
    for tweet in tweets['text']:
        # re.sub(r'[^\x00-\x7f]',r'', tweet)
        tweet = ''.join(filter(lambda x: x in string.printable, tweet))
        #print(tweet)
        #print('\n
        
    return tweets['text'].tolist()

# f = open("facebookTweetsText.txt", "w")
# for tweet in tweets["text"]:
#   f.write("{}\n".format(tweet))
# f.close()

indicoio.config.api_key = '40dc4c756a1582ffe74e549ab29463f2'

tweetsList = tweets['text'].tolist()

start = time.time()
# batch example
a = indicoio.sentiment(tweetsList)
print(a)
#print(a.all())

aggregate_score = 0
total = 0
for i in a:
    total += i
    aggregate_score += i - 0.5
avg = total/len(a)


print (aggregate_score)
approval_rating = avg * 100
print ("Approval Rating: " + str(approval_rating) + "%")
if aggregate_score > 0:
    print("Invest!")
else:
    print("Dont Invest!")
end = time.time()

print (end - start)

#Analysis of Sentiment and Engagement
review = indicoio.analyze_text(tweetsList, apis=['sentiment', 'twitter_engagement'])
#print(b.keys(), b.values())

sentimentArray = np.array(review['sentiment'])
for i in range(len(sentimentArray)):

    sentimentArray[i] = (sentimentArray[i] - 0.5) * 100
engagementArray = np.array(review['twitter_engagement'])

productArray = sentimentArray * engagementArray
print (productArray)

# print (len(productArray))

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

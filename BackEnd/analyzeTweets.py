"""

"""

import json
import pandas as pd
#import matplotlib.pyplot as plt
import re
import string

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

#tweets['stock'] = tweets['text'].apply(lambda tweet: word_in_text('stocks', tweet))
#tweets['trade'] = tweets['text'].apply(lambda tweet: word_in_text('trade', tweet))
#tweets['facebook'] = tweets['text'].apply(lambda tweet: word_in_text('facebook', tweet))
for tweet in tweets['text']:
    #re.sub(r'[^\x00-\x7f]',r'', tweet)
    tweet = ''.join(filter(lambda x: x in string.printable, tweet))
    print (tweet)

#f = open("facebookTweetsText.txt", "w")
#for tweet in tweets["text"]:
 #   f.write("{}\n".format(tweet))
    
#f.close()
    
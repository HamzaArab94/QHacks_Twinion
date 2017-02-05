"""
Code Written By Austin O'Boyle for qHacks 2017
Collaborators: Hamza, Sebastian, Erik

This function takes a text file containing tweets.  These
text files come from piping a twitter stream to a text file.
These files contain empty lines, so those have to be dealt
with.  Thie function creates a new json file with all of the
tweet data
"""

import json
#initialize array of tweets
tweets_data = []
counter = 0
with open("tesla.txt", "r") as tweets_file:
    for line in tweets_file:
        try:
            #skip over empty lines
            if line != '\n' or line != '':
                tweet = json.loads(line)
                #Used to eliminate error where some tweets did
                #not contain a language field
                if 'lang' in tweet:
                    tweets_data.append(tweet)
                    counter += 1
                #limit the number of tweets
                if counter >= 1000:
                    break
        except:
            continue

#Output to similarly named json file
with open("tesla.json", "w") as output:
    json.dump(tweets_data, output)
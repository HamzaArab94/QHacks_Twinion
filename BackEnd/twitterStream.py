"""Code Written by Austin O'Boyle
#Used for Qhacks 2017 Project
#Collaborators: Hamza, Sebastian, Erik

This Code streams live tweets from twitter, filtering them based 
on a topic.  This can be used to pipe tweet data to a text 
file for later analysis
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "827726280074334208-EMt5IOykodLz5MCBQryh5VjqWux5fDv"
access_token_secret = "ZUUSDOAG1CpwqukZCXZCBvcUrsoYk8j0ZW3HX0p8GgGfH"
consumer_key = "11JPAvqF8f6rpLy5LI3UG94du"
consumer_secret = "mPVM202RdkZLxtYt3tvIqnLJpNt1ifsS94X4T40SOIWqE9dTbt"


class StdOutListener(StreamListener):
    #print out data when it is received
    def on_data(self, data):
        print (data)
        return True
        
    #Print out error when there is something going wrong
    def on_error(self, status):
        print("Error {}".format(status))

#Stream for the tweets of a certain topic
def getTweets(topic):
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(languages=["en"], track=[topic])

if __name__ == '__main__':    
    getTweets(topic)
    
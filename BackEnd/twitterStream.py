indicoAPIKey = "6d8a020272686a662976e9afdbf98b82"

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "827726280074334208-EMt5IOykodLz5MCBQryh5VjqWux5fDv"
access_token_secret = "ZUUSDOAG1CpwqukZCXZCBvcUrsoYk8j0ZW3HX0p8GgGfH"
consumer_key = "11JPAvqF8f6rpLy5LI3UG94du"
consumer_secret = "mPVM202RdkZLxtYt3tvIqnLJpNt1ifsS94X4T40SOIWqE9dTbt"

#f = open("allTweets.json", "w")
tweetArray = []
countTweets = 0
class StdOutListener(StreamListener):
    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print("Error {}".format(status))

def getTweets():
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(languages=["en"], track=["donald trump", "Donald Trump"])

if __name__ == '__main__':
    
    getTweets()
    
"""topics_list = ["facebook", "tesla", "donald trump", 
        "hilary clinton", "twitter", "canada", "isis", 
        "syria", "brexit" 
        "snapchat", "instagram","reddit", 
        "police", "dogs", "cats"]"""
    
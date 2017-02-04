indicoAPIKey = "6d8a020272686a662976e9afdbf98b82"

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "827726280074334208-EMt5IOykodLz5MCBQryh5VjqWux5fDv"
access_token_secret = "ZUUSDOAG1CpwqukZCXZCBvcUrsoYk8j0ZW3HX0p8GgGfH"
consumer_key = "11JPAvqF8f6rpLy5LI3UG94du"
consumer_secret = "mPVM202RdkZLxtYt3tvIqnLJpNt1ifsS94X4T40SOIWqE9dTbt"



class StdOutListener(StreamListener):

    def on_data(self, data):
        f.write(data)
        return True

    def on_error(self, status):
        print("Error {}".format(status))


def getCompanyTweets(companyName):
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track = [companyName])

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'

if __name__ == '__main__':
    f = open("facebooktweets.txt", 'w')
    getCompanyTweets("facebook")
    
    
f.close()
    

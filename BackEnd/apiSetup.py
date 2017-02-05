"""
Code written by Austin O'Boyle
Collaborators: Hamza, Erik, Sebastian

This code defines the url and classes for our REST api.  
A user can get at sentiment/emotion/political/personality
data of the users who post tweets of a certain topic
"""
        
        #filename = topic + "Tweets.json"
from flask import Flask
from flask_restful import Resource, Api

#from analyzeTweets import filterTweets, NLPOutput
from analyzeTweets2 import *
import indicoio

app = Flask(__name__)
api = Api(app)
topics_list = ["facebook", "tesla", "donald trump", 
        "hilary clinton", "twitter", "canada", "isis", 
        "syria", "brexit" "snapchat", "instagram","reddit", 
        "police", "dogs", "cats"]
        
class Sentimental(Resource):
    def get(self, topic):
        global topics_list
        
        #These contain lots of tweets about specific topics.
        #Far fewer total tweets than the all.json file
        #Much faster to use than then all.json
        if (topic.lower() in topics_list):
            filename = topic.strip().replace(" ", "_") + ".json"
        
        #all.json used if GET request is for another topic
        else:
            filename = "all.json"
        
        #filter tweets based on keyword
        result = filterTweets(filename, topic, 5)
        #run the tweet list through Indico.io's machine learning
        #API's
        score = sentimentalOutput(result)
        if (score < 0):
            return {'status': 'success', 
                    'result': "People reacted negatively towards this topic"}
        elif (score < 3):
            return {'status': 'success', 
                    'result': "People felt okay about this topic"}
                    
        else:
            return {'status': 'success', 
                    'result': "People felt great about this topic"}
            
class Political(Resource):   
    
    def get(self, topic):
        global topics_list
        if (topic.lower() in topics_list):
            filename = topic.strip().replace(" ", "_") + ".json"
        else:
            filename = "all.json"
            
        result = filterTweets(filename, topic, 5)
        score = politicalOutput(result)
        return {"result":[score]}
        
                    
class Personality(Resource): 
    
    def get(self, topic):
        global topics_list
        if (topic.lower() in topics_list):
            filename = topic.strip().replace(" ", "_") + ".json"
        else:
            filename = "all.json"
            
        result = filterTweets(filename, topic, 5)
        score = personalityOutput(result)
        return {"result":[score]}            

class Emotional(Resource):  
    
    def get(self, topic):
        global topics_list
        if (topic.lower() in topics_list):
            filename = topic.strip().replace(" ", "_") + ".json"
        else:
            filename = "all.json"
            
        result = filterTweets(filename, topic, 5)
        score = emotionalOutput(result)
        return {"result":[score]}
        
#Define url codes for API queries
api.add_resource(Sentimental, '/sentimental/<topic>')
api.add_resource(Political, '/political/<topic>')
api.add_resource(Emotional, '/emotional/<topic>')
api.add_resource(Personality, '/personality/<topic>')


if __name__ == '__main__':
    app.run(debug = True)
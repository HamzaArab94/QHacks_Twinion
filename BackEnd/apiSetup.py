# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 03:11:51 2017

@author: Family
"""
import json
from flask import Flask
from flask_restful import Resource, Api

from analyzeTweets import filterTweets

app = Flask(__name__)
api = Api(app)

class Recommendation(Resource):
    def get(self, topic):
        result = filterTweets('allTweets.txt', topic)
        
        return {'status': 'success', 
                'result': result}
        
api.add_resource(Recommendation, '/recommendation/<topic>')

if __name__ == '__main__':
    app.run(debug = True)
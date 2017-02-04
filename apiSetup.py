from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Recommendation(Resource):
    def get(self, topic):
        return {'status': 'success', 
                'result': ['facebook']}
        
api.add_resource(Recommendation, '/recommendation/<topic>')

if __name__ == '__main__':
    app.run(debug = True)
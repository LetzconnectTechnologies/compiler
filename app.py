from flask import Flask, request
from flask_restful import Resource, Api
from waitress import serve
import time

app = Flask(__name__)
api = Api(app)

class CompilerLogic:
    def __init__(self):
        pass
    
    def process(self, data):
        time.sleep(10)
        return "Code validated"

class Compiler(Resource):
    def get(self):
        return {'status': 'ok'}
    
    def post(self):
        try:
            data = request.get_json()
            language = data['language']
            file_path = data['file_path']
            return {'code':'validated - '+ CompilerLogic().process(data)}
        except Exception as ex:
            print(str(ex))

api.add_resource(Compiler, '/compiler')

if __name__ == '__main__':
    #app.run(debug=True)
    serve(app, port=5000)

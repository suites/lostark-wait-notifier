# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api
from Crawler_lagacy import *

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        cr = Crawler()

        url = "http://loaq.kr/"
        json_file = cr.start(url)

        return json_file

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
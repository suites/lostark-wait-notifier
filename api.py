# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api
from crawler import *

app = Flask(__name__)
api = Api(app)

class TestCrawler(Resource):
    def get(self):
        cr = Crawler()

        json_file = cr.start()

        return json_file

api.add_resource(TestCrawler, '/')

if __name__ == '__main__':
    app.run(debug=True)
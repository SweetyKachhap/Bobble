from flask import Flask
from flask_restful import Api


class AppConfig:
    def __init__(self, class_name):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.app.config['JSON_SORT_KEYS'] = False
        self.api.add_resource(class_name, '/v1/movie/<movieId>')

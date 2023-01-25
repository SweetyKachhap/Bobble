import json
import sys
from flask import Flask, jsonify
from flask_restful import Resource, Api
from DatabaseUtil import Util

app = Flask(__name__)
api = Api(app)
conf_file = sys.argv[1]
conf = json.load(open(conf_file))
try:
    connection = Util(conf["user"], conf["password"], conf["host"], conf["port"], conf["database"])
    print("connected to database")
except Exception as e:
    print("error occurred wile connecting to database", e)


class MovieDetails(Resource):
    def get(self, movieId):
        result = connection.executeQuery(query=f"SELECT * FROM \"MovieDetails\" WHERE \"movieId\" = {movieId}")
        columns = ("id", "title", "poster_path", "language", "overview", "release_date")
        for r in result:
            movie_detail = {columns[i]: r[i] for i, _ in enumerate(r)}
            return jsonify(movie_detail)
        return {"error": "Movie does not found", "error_code": 404}


api.add_resource(MovieDetails, '/v1/movie/<movieId>')


if __name__ == "__main__":
    app.run(debug=True)




from flask import jsonify
from flask_restful import Resource
from bobble.DataCollection.DatabaseConnection import DatabaseConnection
from SetAppConfig import AppConfig


class MovieDetails(Resource):
    def get(self, movieId):
        db_connect = DatabaseConnection()
        result = db_connect.connection.executeQuery(query=f"SELECT * FROM \"MovieDetails\" WHERE \"movieId\" = {movieId}")
        columns = ("id", "title", "poster_path", "language", "overview", "release_date")
        for r in result:
            movie_detail = {columns[i]: r[i] for i, _ in enumerate(r)}
            return jsonify(movie_detail)
        return {"error": "Movie does not found", "error_code": 404}


api_config = AppConfig(MovieDetails)

if __name__ == "__main__":
    api_config.app.run(debug=True)

import json
import sys
from MovieTableSchema import Movies
from DatabaseUtil import Util

data = [
    {"movieId": 1,
     "title": "first_movie",
     "poster_path": "http://first-movie-url-h7t6ydesx",
     "language": "English",
     "overview": "This is a action film, revolves around a fictional character, who is trying to break his own record",
     "release_date": "2020-02-23"},
    {"movieId": 2,
     "title": "second_movie",
     "poster_path": "http://second-movie-url-566tyftr56",
     "language": "Hindi",
     "overview": "This is a drama film, revolves around a family",
     "release_date": "2005-07-04"},
    {"movieId": 3,
     "title": "third_movie",
     "poster_path": "http://third-movie-url-785645eduuy",
     "language": "Telugu",
     "overview": "This is a family drama film, revolves around few fictional character",
     "release_date": "2000-5-20"},
    {"movieId": 4,
     "title": "forth_movie",
     "poster_path": "http://forth-movie-url-8775t6fhguy65",
     "language": "English",
     "overview": "This is a action film, revolves around a life of a boy and his friends",
     "release_date": "2007-09-09"},
]
conf_file = sys.argv[1]
conf = json.load(open(conf_file))

connection = Util(conf["user"], conf["password"], conf["host"], conf["port"], conf["database"])
connection.createTable(Movies)
all_data = []
for each_data in data:
    all_data.append(Movies(each_data["movieId"], each_data["title"], each_data["poster_path"], each_data["language"],
                           each_data["overview"], each_data["release_date"]))

connection.bulk_add(data=all_data)
connection.commit_changes()

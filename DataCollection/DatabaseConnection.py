from bobble.DataCollection.DatabaseUtil import Util
import sys
import json


class DatabaseConnection:

    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        conf_file = sys.argv[1]
        conf = json.load(open(conf_file))
        try:
            connection = Util(conf["user"], conf["password"], conf["host"], conf["port"], conf["database"])
            print("connected to database")
            return connection
        except Exception as e:
            print("error occurred wile connecting to database", e)
            return e

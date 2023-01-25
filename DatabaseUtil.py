from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Util:
    def __init__(self, user, password, host='localhost', port=5432, database='postgres'):
        self.engin = create_engine("postgresql://"+user+":"+password+"@"+host+":"+str(port)+"/"+database)
        self.session = self.__create_session()

    def __create_session(self):
        Session = sessionmaker()
        Session.configure(bind=self.engin)
        session = Session()
        return session

    def createTable(self, table):
        Base = declarative_base()
        table_objects = [table.__table__]
        Base.metadata.create_all(self.engin, tables=table_objects)

    def executeQuery(self, query):
        result = self.session.execute(query)
        return result

    def bulk_add(self, data):
        self.session.add_all(data)

    def commit_changes(self):
        try:
            self.session.commit()
            print("Changes committed")
        except Exception as error:
            print(f"An error occurred:{error} ---- type:{type(error)}")
            return False

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, VARCHAR, Date

Base = declarative_base()


class Movies(Base):
    __tablename__ = "MovieDetails"
    movieId = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(100), nullable=False)
    poster_path = Column(String(100))
    language = Column(String(50))
    overview = Column(VARCHAR(1000))
    release_date = Column(Date)

    def __init__(self, movieId, title, poster_path, language, overview, release_date):
        self.movieId = movieId
        self.title = title
        self.poster_path = poster_path
        self.language = language
        self.overview = overview
        self.release_date = release_date

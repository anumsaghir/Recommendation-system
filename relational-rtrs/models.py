from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True)
    title = Column(Unicode(500))
    genres = Column(Unicode(500))

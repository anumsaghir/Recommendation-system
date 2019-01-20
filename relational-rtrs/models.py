from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Unicode, Float
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True)
    title = Column(Unicode(500))
    genres = Column(Unicode(500))


class Rating(Base):
    __tablename__ = 'ratings'

    user_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, primary_key=True)
    rating = Column(Float)
    timestamp = Column(Integer)


class Tag(Base):
    __tablename__ = 'tags'

    user_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, primary_key=True)
    tags = Column(Unicode(500))
    timestamp = Column(Integer)


def get_db():
    engine = create_engine('mysql+pymysql://anum:pakistan@localhost/movies_db')
    Session = sessionmaker(bind=engine)

    return Session()

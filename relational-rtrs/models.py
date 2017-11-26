from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Unicode, Float
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True)
    title = Column(Unicode(500))
    genres = Column(Unicode(500))


class Similarity(Base):
    __tablename__ = 'similarities'

    movie_id_1 = Column(Integer, primary_key=True)
    movie_id_2 = Column(Integer, primary_key=True)
    similarity_index = Column(Float)


def get_db():
    engine = create_engine('mysql+pymysql://anum:pakistan@localhost/movies_db')
    Session = sessionmaker(bind=engine)

    return Session()

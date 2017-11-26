from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Unicode
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True)
    title = Column(Unicode(500))
    genres = Column(Unicode(500))

class Similarities(Base):
    __tablename__ = 'similarities'

    movie_id_1 = Column(Integer)
    movie_id_2 = Column(Integer)
    similarity_index = Column(float) 
    PRIMARY KEY(user_id, movie_id)
     


def get_db():
    engine = create_engine('mysql+pymysql://anum:pakistan@localhost/movies_db')
    Session = sessionmaker(bind=engine)

    return Session()

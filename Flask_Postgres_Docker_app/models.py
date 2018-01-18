from sqlalchemy import Column, String, Integer, ForeignKey  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import os

user = os.environ['POSTGRES_USER']
passwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = 'db'
port='5432'

# get the postgresql database url
engine = create_engine('postgresql://{user1}:{passwd1}@{host1}:{port1}/{db1}'.format(
        user1=user,
        passwd1=passwd,
        host1=host,
        port1=port,
        db1=db))

# bind the postgres to the session 
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# # simple movie table
# class User(Base):
# 	__tablename__ = 'movie_table'

# 	id = Column(Integer, primary_key=True)
# 	name = Column(String(250), unique=True, nullable=False)
# 	moviename = Column(String(250), nullable=False)
class User(Base):
	__tablename__ = 'roleplayer'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(250), unique=True, nullable=True)
	movie = relationship('Movie', backref='roleplayer')


class Movie(Base):
	__tablename__ = 'movie'

	id = Column(Integer, primary_key=True, autoincrement=True)
	moviename = Column(String(250), nullable=False)
	movie_releaseyear = Column(Integer)
	movie_imdb = Column(String(500), nullable=False)
	roleid = Column(Integer, ForeignKey('roleplayer.id'))


def __init__database():
	# create all the database tables
	Base.metadata.create_all(engine)


# # engine = create_engine('postgresql://saranya:mynewpassword@localhost/movie_db')
# # bind the postgres to the session 
# Session = sessionmaker(bind=engine)
# session = Session()

# Base = declarative_base()

# class User(Base):
# 	__tablename__ = 'movie_table'

# 	id = Column(Integer, primary_key=True)
# 	name = Column(String(250), unique=True, nullable=False)
# 	moviename = Column(String(250), nullable=False)


# def __init__database():
# 	# create all the database tables
# 	Base.metadata.create_all(engine)

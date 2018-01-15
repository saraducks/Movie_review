from sqlalchemy import Column, String, Integer, ForeignKey  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

POSTGRES_USER='saranya'
POSTGRES_DATABASE='movie_db'
POSTGRES_PASSWD='mynewpassword'
POSTGRES_HOST = '192.168.99.100'
POSTGRES_PORT = '5432'

# get the postgresql database url
engine = create_engine('postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=POSTGRES_USER,
        passwd=POSTGRES_PASSWD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        db=POSTGRES_DATABASE))
print(engine)
# engine = create_engine('postgresql://saranya:mynewpassword@localhost/movie_db')
# bind the postgres to the session 
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# simple movie table
class User(Base):
	__tablename__ = 'movie_table'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), unique=True, nullable=False)
	moviename = Column(String(250), nullable=False)

# create all the database tables
Base.metadata.create_all(engine)

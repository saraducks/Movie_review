from sqlalchemy import Column, String, Integer, ForeignKey  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# get the postgresql database url
engine = create_engine('postgresql://saranya:mynewpassword@localhost/movie_db')
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

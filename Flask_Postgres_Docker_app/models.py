from sqlalchemy import Column, String, Integer, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from sqlalchemy.types import ARRAY, Float
import psycopg2


# import os

# user = os.environ['POSTGRES_USER']
# passwd = os.environ['POSTGRES_PASSWORD']
# db = os.environ['POSTGRES_DB']
# host = 'db'
# port='5432'

# get the postgresql database url
# engine = create_engine('postgresql://{user1}:{passwd1}@{host1}:{port1}/{db1}'.format(
#         user1=user,
#         passwd1=passwd,
#         host1=host,
#         port1=port,
#         db1=db))

engine = create_engine('postgresql://saranya:mynewpassword@localhost/movie_db')
# bind the postgres to the session 
Session = sessionmaker(bind=engine)
multi_thrdconn = scoped_session(Session)
session = Session()

Base = declarative_base()

# # simple movie table
# class User(Base):
# 	__tablename__ = 'movie_table'

# 	id = Column(Integer, primary_key=True)
# 	name = Column(String(250), unique=True, nullable=False)
# 	moviename = Column(String(250), nullable=False)

class Movie(Base):
	__tablename__ = 'movie1'

	id = Column(Integer, primary_key=True, nullable=True)
	movieimdbid = Column(String(300), unique=True)
	movie_title = Column(String(300), nullable=False)
	movie_rating = Column(Float, nullable=False)
	movie_releaseyear = Column(Integer)
	movie_votes = Column(Integer)

class User(Base):
	__tablename__ = 'roleplayer'

	id = Column(Integer, primary_key=True, nullable=True)
	role_id = Column(String(250), unique=True)
	name = Column(String(250), nullable=True)
	birthyear = Column(Integer, nullable=True)
	deathyear = Column(Integer, nullable=True)
	primaryprofession = Column(String, nullable=True)
	movies_acted = Column(String)

	# id = Column(Integer, primary_key=True, autoincrement=True)
	# moviename = Column(String(250), nullable=False)
	# movie_releaseyear = Column(Integer)
	# movie_imdb = Column(String(500), nullable=False)
	# roleid = Column(Integer, ForeignKey('roleplayer.id'))

Base.metadata.create_all(engine)

SQL_Movie = """ 
        COPY movie1(movieimdbid, movie_title, movie_rating, movie_releaseyear,movie_votes) FROM STDIN WITH
        DELIMITER '\t' 
			"""

SQL_Role = """
		COPY roleplayer(role_id, name, birthyear, deathyear, primaryprofession,movies_acted) FROM STDIN WITH
        DELIMITER '\t'
           """
db_conn = session.connection().connection.cursor()

f_movie = open('data_model/movie.tsv')
f_role = open('data_model/name.basics.tsv')

db_conn = psycopg2.connect(database='movie_db', user='saranya')

def generate_table_contents(SQL_Movie, SQL_Role,f_movie, f_role):
	cursor = db_conn.cursor()
	try:
		cursor.copy_expert(sql=SQL_Movie,file=f_movie)
		cursor.execute("commit;")
		cursor.copy_expert(sql=SQL_Role, file=f_role)
		cursor.execute("commit;")
		cursor.close()
	except:
		cursor.close()
# cursor.copy_expert("COPY Movie(movieimdbid, movie_title, movie_rating, movie_releaseyear,movie_votes) FROM '/Users/sara/Downloads/test_Movie_review/Flask_Postgres_Docker_app/data_model/movie.tsv' WITH DELIMITER '' CSV HEADER")
# cursor.copy_expert("COPY User(role_id, name, birthyear, deathyear, primaryprofession,movies_acted) FROM '/Users/sara/Downloads/test_Movie_review/Flask_Postgres_Docker_app/data_model/name.basics.tsv'")
# def __init__database():
# 	# create all the database tables
# 	Base.metadata.create_all(engine)
try:
	generate_table_contents(SQL_Movie, SQL_Role, f_movie, f_role)
finally:
	db_conn.close()


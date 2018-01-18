from flask import Flask, request, render_template, redirect, url_for
from models import *
from models import User, Movie, engine

app = Flask(__name__)

# create a new row in the movie table 
@app.route('/main/createnewmovie', methods=['GET', 'POST'])
def create_movie():
	if request.method == 'POST':
		# check if the user already exists
		check_existing_user = session.query(User.id).filter(User.name==request.form['actor_name']).scalar()
		check_movie_exists = session.query(Movie).filter(Movie.moviename == request.form['movie-name']).scalar()
		if check_existing_user and check_movie_exists:
			return "Movie and the role player already exists! Thanks for participation!"
		elif check_existing_user:
			# add new movie
			add_newmovie = Movie(moviename=request.form['movie-name'], movie_releaseyear=request.form['release-year'], movie_imdb=request.form['imdb-link'], roleid=check_existing_user.id)
			session.add(add_newmovie)
			session.commit()
			return redirect(url_for('hello'))
		# else create a new row in the User table
		else:
			add_newuser = User(name=request.form['actor_name'])
			session.add(add_newuser)
			session.commit() 
			add_newmovie = Movie(moviename=request.form['movie-name'], movie_releaseyear=request.form['release-year'], movie_imdb=request.form['imdb-link'], roleid=add_newuser.id)
			session.add(add_newmovie)
			session.commit()
			return redirect(url_for('hello'))
	# diaply the form to create a new movie row 
	else:
		return render_template('main.html')

@app.route('/search', methods=['GET', 'POST'])
def search_page():
	if request.method == 'POST':
		if len(request.form['search_movie']) > 0:
			return redirect(url_for('display_movie', searchmovie=request.form['search_movie']))
		elif len(request.form['role_name']) > 0:
			return redirect(url_for('display_role', searchrole=request.form['role_name']))
	else:
		return render_template('searchpage.html')

@app.route('/displayrole/<searchrole>', methods=['POST', 'GET'])
def display_role(searchrole):
	print("Search rolesssss", searchrole)
	get_role_name = session.query(User.id, User.name).filter(User.name==searchrole)
	if get_role_name.scalar() is not None:
		return render_template('display_roleplayer.html', display=get_role_name)
	else:
		return "role player doesn't exist in our database"

@app.route('/displaymovie/<searchmovie>', methods=['POST', 'GET'])
def display_movie(searchmovie):
	get_movie = session.query(Movie).filter(Movie.moviename==searchmovie)
	if get_movie.scalar() is not None:
		return render_template('display_movie.html', display=get_movie)
	else:
		return "Movie doesn't exist in the database"

@app.route('/')
def hello():
	return "hello successfully created the new movie!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
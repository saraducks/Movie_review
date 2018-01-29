from flask import Flask, request, render_template, redirect, url_for, jsonify
from models import User, Movie, engine, session, create_engine
import webbrowser

app = Flask(__name__)

engine = create_engine('postgresql://saranya:mynewpassword@localhost/movie_db')
db_conn= engine.connect()


# for the web
# create a new row in the movie table 
@app.route('/main/createnewmovie', methods=['GET', 'POST'])
def create_movie():
	if request.method == 'POST':
		# check if the user already exists
		check_existing_user = session.query(User.id).filter(User.name==request.form['actor_name']).scalar()
		check_movie_exists = session.query(Movie).filter(Movie.movie_title == request.form['movie-name']).scalar()
		if check_existing_user and check_movie_exists:
			return "Movie and the role player already exists! Thanks for participation!"
		elif check_existing_user:
			# add new movie
			add_newmovie = Movie(movieimdbid=request.form['movie-imdb'],movie_title=request.form['movie-name'], movie_rating=request.form['ratings'],movie_releaseyear=request.form['release-year'],movie_votes=request.form['votes'])
			session.add(add_newmovie)
			session.commit()
			return redirect(url_for('movieimdb_status'))
		# else create a new row in the User table
		else:
			add_newmovie = Movie(movieimdbid=request.form['movie-imdb'],movie_title=request.form['movie-name'], movie_rating=request.form['ratings'],movie_releaseyear=request.form['release-year'],movie_votes=request.form['votes'])
			session.add(add_newmovie)
			session.commit()
			#find movie imdb id
			imdb_movie_getid = session.query(Movie).filter(Movie.movies_acted==request.form['acted'])			
			add_newuser = User(name=request.form['actor_name'], birthyear=request.form['birthday'],deathyear=request.form['deathday'], primaryprofession=request.form['proff'], movies_acted=request.form['acted'])
			session.add(add_newuser)
			session.commit() 
			return redirect(url_for('movieimdb_status'))
	# diaply the form to create a new movie row 
	else:
		return render_template('main.html')

# search from the webbrowser end for either using movie name or role name
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
	get_role_name = session.execute("SELECT * FROM roleplayer WHERE name='%s';" % (searchrole))
	get_role_namecount = session.execute("SELECT * FROM roleplayer WHERE name='%s';" % (searchrole)).scalar()
	if get_role_namecount is not None:
		return render_template('display_roleplayer.html', display=get_role_name)
	else:
		return "role player doesn't exist in our database"

@app.route('/displaymovie/<searchmovie>', methods=['POST', 'GET'])
def display_movie(searchmovie):
	get_movie = session.query(Movie).filter(Movie.movie_title==searchmovie)
	if get_movie.scalar() is not None:
		return render_template('display_movie.html', display=get_movie)
	else:
		return "Movie doesn't exist in the database"

# for api search
@app.route('/apisearch', methods=['GET', 'POST'])
def search():
	# check the param if the search is based on movie or roleplayer
	if request.method == 'GET':
		if request.args.get('search_movie') is not None:
			return displaymovie_api(request.args.get('search_movie'))
		if request.args.get('search_role') is not None:
			return displayrole_api(request.args.get('search_role'))

	
@app.route('/movie/roleplayer', methods=['POST', 'GET'])
def displayrole_api(searchrole):
	get_role_name = session.execute("SELECT * FROM roleplayer WHERE name='%s';" % (searchrole))	
	get_role_name_count = session.execute("SELECT * FROM roleplayer WHERE name='%s';" % (searchrole)).scalar()

	if get_role_name_count > 0:                                                         #if the count is greater than 0, then result exists and extract the movie based on the role player acted columnresult
		json_string = {"Role Player":[], "Movies acted":[]}
        
        for i in get_role_name:
        	json_string["Role Player"].append([{"Name": i.name, "Birthyear":i.birthyear, "primaryprofession":i.primaryprofession}])
        
        get_movies_acted = session.execute("SELECT movies_acted FROM roleplayer WHERE name='%s';" % (searchrole))

        for k in get_movies_acted:
	    	res = k[0].split(',')
	    	for i in res:
	    		acted_movies_count = session.execute("SELECT * FROM movie1 WHERE movieimdbid='%s';" % (i)).scalar()
	    		if acted_movies_count > 0:
	    			acted_movies = session.execute("SELECT * FROM movie1 WHERE movieimdbid='%s';" % (i.encode("utf-8")))
	    			for cols in acted_movies:
	    				json_string["Movies acted"].append([{'Title':cols.movie_title, 'imdb_id':cols.movieimdbid, 'Released_on':cols.movie_releaseyear, 'Ratings':cols.movie_rating,'votes':cols.movie_votes}])
			
		return jsonify(json_string)
	else:
		return "role player doesn't exist in our database"


@app.route('/movie/moviedescription', methods=['POST', 'GET'])
def displaymovie_api(searchmovie):
	get_movie = session.execute("SELECT * FROM movie1 WHERE movie_title='%s';" % (searchmovie))
	get_no_of_movies = session.execute("SELECT * FROM movie1 WHERE movie_title='%s';" % (searchmovie)).scalar()
	json_string = {"Movie details": []}
	if get_no_of_movies > 0:
		for i in get_movie:
			json_string['Movie details'].append([{'Title':i.movie_title, 'imdb_id':i.movieimdbid, 'Released_on':i.movie_releaseyear, 'Ratings':i.movie_rating,'votes':i.movie_votes}])
		return jsonify(json_string)
	else:
		return "Movie doesn't exist in the database"

@app.route('/imdbredirect/<movieimdb_id>')
def imdbpage(movieimdb_id):
	return redirect(webbrowser.open("http://www.imdb.com/title/%s"%(movieimdb_id)))

@app.route('/movieimdb_status')
def movieimdb_status():
	return "hello successfully created the new movie!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
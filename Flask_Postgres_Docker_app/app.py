from flask import Flask, request, render_template, redirect, url_for
from models import *
from models import User

app = Flask(__name__)

# create a new row in the movie table 
@app.route('/main/createnewmovie', methods=['GET', 'POST'])
def create_movie():
	if request.method == 'POST':
		# check if the user already exists
		check_existing_user = session.query(User).filter(User.name==request.form['actor_name'])
		if check_existing_user:
			return redirect(url_for('display_warning'))
		# else create a new row in the User table
		else:
			add_new_movie = User(name=request.form['actor_name'], moviename=request.form['movies'])
			session.add(add_new_movie)
			session.commit() 
			return redirect(url_for('hello'))
	# diaply the form to create a new movie row 
	else:
		return render_template('main.html')

# already existing user in the database
@app.route('/alreadyexists')
def display_warning():
	return "Actor/Actress is already existing in the database"

@app.route('/')
def hello():
	return "hello successfully created the new movie!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
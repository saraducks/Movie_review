from flask import Flask, request, render_template, redirect
from models import *
from models import User

app = Flask(__name__)

@app.route('/main/createnewmovie', methods=['GET', 'POST'])
def create_movie():
	if request.method == 'POST':
		# check if the user already exists
		check_existing_user = session.query(User).filter(User.name == request.form['actor_name'])
		print(check_existing_user.name, "))))))))))))))))(((((((((((((")
		if check_existing_user == request.form['actor_name']:
			return redirect(url_for('/'))
		else:
			add_new_movie = User(name=request.form['actor_name'], moviename=request.form['movies'])
			session.add(add_new_movie)
			session.commit() 
			return redirect(url_for('/'))
	else:
		return render_template('main.html')

@app.route('/')
def hello():
	return "hello successfully created the new movie!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
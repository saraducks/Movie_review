Simple Flask-Postgres-Docker application demo.

# Stack

  Nginx
  Flask
  Docker
  Postgres


# Flask-Nginx-Docker-Postgres simple application
  Docker compose multi conatiner helps to install the required web server, flask and postgres. Run the following command:
    
    docker-compose build     
    docker-compose -f docker-compose.yml up -d 
    docker-compose run flaskapp /bin/bash -c "cd /app/Flask_Postgres_Docker_app && python models.py"

  The nginx webserver serves the client requests and forward it to the docker conatiner which in turn forward the request to the flask application that is running as a demon.  

# Postgres Connection setup
  The flask app connects to the postgres using the Sqlalchemy(ORM). To connect to the postgres, add the required field in the env file with the respective usre's postgres credentials.

  engine = create_engine('postgresql://%s:%s@%s:%s/%s' % (user, passwd, host, port, db)) and the env variables will be used to populate the respective fields in the create_engine parameters. engine will allow the SqlAlchemy to access the DataBase.


# Docker
  Docker file is used within the docker-compose to get the application requirements and ready for running the app.
  Docker compose installs and inter-connects the webserver to the backend service.  

# Nginx
  Nginx used as a proxy webserver which serves the request and forwards to the docker conatiner. Make sure to change the config.d file with your configuration file. 

# API URL
  Search based on role player

  GET  http://0.0.0.0:5000/apisearch?search_role=Ryan Gosling

  Result will be:

        {
        "Movies acted": [
          [
            {
              "Ratings": 7.8, 
              "Released_on": 2011, 
              "Title": "Drive", 
              "imdb_id": "tt0780504", 
              "votes": 483028
            }
          ], 
          [
            {
              "Ratings": 8.1, 
              "Released_on": 2016, 
              "Title": "La La Land", 
              "imdb_id": "tt3783958", 
              "votes": 340469
            }
          ], 
          [
            {
              "Ratings": 7.4, 
              "Released_on": 2010, 
              "Title": "Blue Valentine", 
              "imdb_id": "tt1120985", 
              "votes": 157792
            }
          ], 
          [
            {
              "Ratings": 7.9, 
              "Released_on": 2004, 
              "Title": "The Notebook", 
              "imdb_id": "tt0332280", 
              "votes": 438209
            }
          ]
        ], 
        "Role Player": [
          [
            {
              "Birthyear": 1980, 
              "Name": "Ryan Gosling", 
              "primaryprofession": "actor,soundtrack,producer"
            }
          ]
        ]
        }
  Search based on Movie

  GET  http://0.0.0.0:5000/search?search_movie=Un bon bock






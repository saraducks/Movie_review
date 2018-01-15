Simple python-flask application running in a docker container.

# Movie_review
  Display the movie with the reviews using Flask, SqlAlchemy, Postgres, Python.

# Postgres Connection setup
  Connect the flaks app to the postgres using the Sqlalchemy(ORM). The set up are dynamically passed on Docker run command via PSQL_USRNAME, PSQL_PASSWD, PSQL_DBNAME

  docker run --env PSQL_USRNAME=<YOUR_USERNAME> --env PSQL_PASSWD=<YOUR_PASSWD> --env PSQL_DBNAME=<YOUR_DBNAME>

  The docker run will kick the app.py and It will be accessed at the url: https://127.0.0.1:5000

# Docker
   Docker is used for the fast provisioning of the source instances 
   
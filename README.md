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
  	docker-compose run flaskapp /bin/bash -c "cd /app/Flask_Postgres_Docker_app && python -c 'import models; models.__init__database()'"

  The nginx webserver used for serving the client requests and forward it to the flask application.  

# Postgres Connection setup
  The flask app connects to the postgres using the Sqlalchemy(ORM). To connect to the postgres, add the required field in the env file with the respective usre's postgres credentials.


# Docker
   Docker file is used within the docker-compose to get the application requirements and ready for running the app.
   Docker compose installs and inter-connects the webserver to the backend service.  
   
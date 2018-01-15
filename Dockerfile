FROM python:3.6.1

COPY requirements.txt /
RUN pip install -r ./requirements.txt

COPY My_app/ /app/
WORKDIR /app

ENV FLASK_APP=app.py
EXPOSE 5000
CMD flask run 

FROM python:3.6.1

RUN mkdir -p /app

COPY requirements.txt /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5000
CMD ["python", "./Flask_Postgres_Docker_app/app.py"]

FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install pytest psycopg2

CMD ["pytest", "-v", "db_tests.py"]
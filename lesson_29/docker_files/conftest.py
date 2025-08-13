import psycopg2
import os
import time
import pytest


@pytest.fixture(scope="module")
def db_connection():
    time.sleep(5)
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )
    yield conn
    conn.close()

@pytest.fixture(scope="module", autouse=True)
def setup_database(db_connection):
    cur = db_connection.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        );
    """)
    db_connection.commit()
    cur.close()
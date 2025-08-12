import psycopg2
import os
import time
import pytest

time.sleep(5)

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def test_insert():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES ('Lina') RETURNING id;")
    inserted_id = cur.fetchone()[0]
    conn.commit()

    cur.execute("SELECT name FROM users WHERE id=%s;", (inserted_id,))
    result = cur.fetchone()
    assert result[0] == 'Lina'
    cur.close()
    conn.close()


def test_update():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES ('OldName') RETURNING id;")
    conn.commit()
    cur.execute("UPDATE users SET name='NewName' WHERE name='OldName';")
    conn.commit()

    cur.execute("SELECT name FROM users WHERE name='NewName';")
    result = cur.fetchone()
    assert result is not None and result[0] == 'NewName'
    cur.close()
    conn.close()


def test_delete():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES ('ToDelete') RETURNING id;")
    conn.commit()
    cur.execute("DELETE FROM users WHERE name='ToDelete';")
    conn.commit()

    cur.execute("SELECT * FROM users WHERE name='ToDelete';")
    result = cur.fetchone()
    assert result is None
    cur.close()
    conn.close()


def test_select_empty():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users;")
    count = cur.fetchone()[0]
    assert isinstance(count, int)
    cur.close()
    conn.close()
def test_insert(db_connection):
    cur = db_connection.cursor()
    cur.execute("INSERT INTO users (name) VALUES ('Lina') RETURNING id;")
    inserted_id = cur.fetchone()[0]
    db_connection.commit()

    cur.execute("SELECT name FROM users WHERE id=%s;", (inserted_id,))
    result = cur.fetchone()
    assert result[0] == 'Lina'
    cur.close()


def test_update(db_connection):
    cur = db_connection.cursor()
    cur.execute("INSERT INTO users (name) VALUES ('OldName') RETURNING id;")
    db_connection.commit()

    cur.execute("UPDATE users SET name='NewName' WHERE name='OldName';")
    db_connection.commit()

    cur.execute("SELECT name FROM users WHERE name='NewName';")
    result = cur.fetchone()
    assert result is not None and result[0] == 'NewName'
    cur.close()


def test_delete(db_connection):
    cur = db_connection.cursor()
    cur.execute("INSERT INTO users (name) VALUES ('ToDelete') RETURNING id;")
    db_connection.commit()

    cur.execute("DELETE FROM users WHERE name='ToDelete';")
    db_connection.commit()

    cur.execute("SELECT * FROM users WHERE name='ToDelete';")
    result = cur.fetchone()
    assert result is None
    cur.close()


def test_select_empty(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM users;")
    count = cur.fetchone()[0]
    assert isinstance(count, int)
    cur.close()
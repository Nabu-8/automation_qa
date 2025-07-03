import sqlite3
import os
from constants import BASE_DIR

db_path = BASE_DIR / 'sqlite_db.sqlite'

if os.path.exists(db_path):
    os.remove(db_path)

connection = None
cursor = None

try:
    connection = sqlite3.connect(str(db_path))
    print("DB was created!")

    cursor = connection.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    create_categories_table = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER NOT NULL,
            name TEXT NOT NULL,
            is_active BOOLEAN NOT NULL,
            CONSTRAINT categories_pk PRIMARY KEY (id)
        );
        """

    create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category_id INTEGER NOT NULL,
            CONSTRAINT products_pk PRIMARY KEY (id),
            CONSTRAINT products_category_fk FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        );
        """

    cursor.execute(create_categories_table)
    cursor.execute(create_products_table)

    categories = [
        (1, 'Dog food', True),
        (2, 'Cat food', True),
        (3, 'Bird food', False)
    ]

    products = [
        (1, 'Purina Pro Plan Adult Large Breed', 'High-protein dry dog food.', 59.99, 1),
        (2, 'Royal Canin Indoor 27', None, 49.50, 2),
        (3, 'Parrot Mix Premium', 'Grain mix for parrots.', 29.90, 3)
    ]


    cursor.executemany(
        'INSERT OR IGNORE INTO categories (id, name, is_active) VALUES (?, ?, ?)',
        categories
    )
    cursor.executemany(
        'INSERT OR IGNORE INTO products (id, name, description, price, category_id) VALUES (?, ?, ?, ?, ?)',
        products
    )

    connection.commit()

    cursor.execute(''' SELECT "products"."id", "products"."name", "products"."description", 
      "products"."price", "categories"."name", "categories"."is_active" FROM "products"
    JOIN "categories" ON "products"."category_id" = "categories"."id";
    ''')
    rows = cursor.fetchall()
    print("Products with categories:")
    for row in rows:
        row = list(row)
        row[5] = bool(row[5])
        print(tuple(row))

except Exception as error:
    print("Error while connecting to Sqlite3", error)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("SQLITE3 connection is closed")
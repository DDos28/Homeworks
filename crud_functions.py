import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
          id INTEGER PRIMARY KEY,
          title TEXT NOT NULL,
          description TEXT,
          price INTEGER NOT NULL
        )
    ''')
    conn.commit()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()

initiate_db()
cursor.execute('DELETE FROM Products')

cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Продукт 1', 'Описание 1', 100)")
cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Продукт 2', 'Описание 2', 200)")
cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Продукт 3', 'Описание 3', 300)")
cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Продукт 4', 'Описание 4', 400)")
conn.commit()



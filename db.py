import sqlite3 as db

def connect_db():
    return db.connect('library.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT,
            Author  TEXT,
            Availability BOOLEAN
)
''')

create_tables()
print('db connected')
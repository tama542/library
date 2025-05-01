import sqlite3 as db

def connect_db():
    return db.connect('library.db')

def add_books():
    books =[
        {"Title": "The Ending", "Author": "Michael Kross", "Availability": "True"}
    ]


conn = connect_db()
c = conn.cursor()

add_books()

print('book added')
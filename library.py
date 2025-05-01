# class Library:
#     def __init__(self):
#         self.connection = sqlite3.connect("library.db")
#         self.cursor = self.connection.cursor()

#     def add_book(self, title, author, isbn):
#         try:
#             self.cursor.execute(
#                 "INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)",
#                 (title, author, isbn)
#             )
#             self.connection.commit()
#             print(f"Book '{title}' added successfully.")
#         except sqlite3.IntegrityError:
#             print("Book with the same ISBN already exists.")

#     def register_user(self, name, user_id):
#         try:
#             self.cursor.execute(
#                 "INSERT INTO users (name, user_id) VALUES (?, ?)",
#                 (name, user_id)
#             )
#             self.connection.commit()
#             print(f"User '{name}' registered successfully.")
#         except sqlite3.IntegrityError:
#             print("User with the same ID already exists.")

#     def checkout_book(self, user_id, isbn):
#         self.cursor.execute("SELECT id, is_available FROM books WHERE isbn = ?", (isbn,))
#         book = self.cursor.fetchone()
#         self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
#         user = self.cursor.fetchone()

#         if book and user and book[1]:
#             self.cursor.execute(
#                 "UPDATE books SET is_available = 0 WHERE id = ?",
#                 (book[0],)
#             )
#             self.connection.commit()
#             print(f"Book with ISBN '{isbn}' checked out by User ID '{user_id}'.")
#         elif not book:
#             print(f"Book with ISBN '{isbn}' not found.")
#         elif not user:
#             print(f"User with ID '{user_id}' not found.")
#         else:
#             print(f"Book with ISBN '{isbn}' is currently unavailable.")

#     def return_book(self, isbn):
#         self.cursor.execute("SELECT id FROM books WHERE isbn = ?", (isbn,))
#         book = self.cursor.fetchone()

#         if book:
#             self.cursor.execute(
#                 "UPDATE books SET is_available = 1 WHERE id = ?",
#                 (book[0],)
#             )
#             self.connection.commit()
#             print(f"Book with ISBN '{isbn}' returned successfully.")
#         else:
#             print(f"Book with ISBN '{isbn}' not found in the library database.")

#     def display_books(self):
#         self.cursor.execute("SELECT title, author, isbn, is_available FROM books")
#         books = self.cursor.fetchall()
#         print("Books in Library:")
#         for book in books:
#             status = "Available" if book[3] else "Checked Out"
#             print(f"Title: {book[0]}, Author: {book[1]}, ISBN: {book[2]}, Status: {status}")

#     def display_users(self):
#         self.cursor.execute("SELECT name, user_id FROM users")
#         users = self.cursor.fetchall()
#         print("Registered Users:")
#         for user in users:
#             print(f"Name: {user[0]}, User ID: {user[1]}")

#     def close_connection(self):
#         self.connection.close()


import json

def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file)

def add_book(title, author):
    books = load_books()
    books[title] = author
    save_books(books)
    print(f"Book '{title}' by {author} added.")

def remove_book(title):
    books = load_books()
    if title in books:
        del books[title]
        save_books(books)
        print(f"Book '{title}' removed.")
    else:
        print(f"Book '{title}' not found.")

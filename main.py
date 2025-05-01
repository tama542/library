
import tkinter as tk
from tkinter import messagebox, Listbox
import json

class Library:
    def __init__(self):
        self.books = self.load_data("books.json")  # Book inventory
        self.users = self.load_data("users.json")  # User data

    @staticmethod
    def load_data(filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_data(data, filename):
        with open(filename, "w") as file:
            json.dump(data, file)

    def add_book(self, title, copies):
        if title in self.books:
            self.books[title] += copies
        else:
            self.books[title] = copies
        self.save_data(self.books, "books.json")
        messagebox.showinfo("Success", f"Book '{title}' added with {copies} copies.")

    def delete_book(self, title):
        if title in self.books:
            del self.books[title]
            self.save_data(self.books, "books.json")
            messagebox.showinfo("Success", f"Book '{title}' deleted.")
        else:
            messagebox.showerror("Error", f"Book '{title}' not found.")

    def register_user(self, name):
        if name in self.users:
            messagebox.showwarning("Warning", f"User '{name}' already exists.")
        else:
            self.users[name] = []
            self.save_data(self.users, "users.json")
            messagebox.showinfo("Success", f"User '{name}' registered.")

    def borrow_book(self, name, title):
        if name in self.users:
            if title in self.books and self.books[title] > 0:
                if len(self.users[name]) < 3:
                    self.users[name].append(title)
                    self.books[title] -= 1
                    self.save_data(self.books, "books.json")
                    self.save_data(self.users, "users.json")
                    messagebox.showinfo("Success", f"Book '{title}' borrowed by '{name}'.")
                else:
                    messagebox.showerror("Error", "Borrowing limit reached (3 books).")
            else:
                messagebox.showerror("Error", f"Book '{title}' is unavailable.")
        else:
            messagebox.showerror("Error", f"User '{name}' is not registered.")

    def return_book(self, name, title):
        if name in self.users:
            if title in self.users[name]:
                self.users[name].remove(title)
                self.books[title] += 1
                self.save_data(self.books, "books.json")
                self.save_data(self.users, "users.json")
                messagebox.showinfo("Success", f"Book '{title}' returned by '{name}'.")
            else:
                messagebox.showerror("Error", f"'{name}' has not borrowed '{title}'.")
        else:
            messagebox.showerror("Error", f"User '{name}' is not registered.")

# Tkinter GUI with Styling
library = Library()

# Styling Functions
def add_book_ui():
    title = book_title_entry.get()
    copies = book_copies_entry.get()
    if title and copies.isdigit():
        library.add_book(title, int(copies))
    else:
        messagebox.showerror("Error", "Please provide valid book title and copies.")

def delete_book_ui():
    title = book_title_entry.get()
    if title:
        library.delete_book(title)
    else:
        messagebox.showerror("Error", "Please provide a valid book title.")

def register_user_ui():
    name = user_name_entry.get()
    if name:
        library.register_user(name)
    else:
        messagebox.showerror("Error", "Please provide a valid user name.")

def borrow_book_ui():
    name = user_name_entry.get()
    title = book_title_entry.get()
    if name and title:
        library.borrow_book(name, title)
    else:
        messagebox.showerror("Error", "Please provide valid user name and book title.")

def return_book_ui():
    name = user_name_entry.get()
    title = book_title_entry.get()
    if name and title:
        library.return_book(name, title)
    else:
        messagebox.showerror("Error", "Please provide valid user name and book title.")

def view_books_ui():
    books = library.books
    books_list.delete(0, tk.END)
    for title, copies in books.items():
        books_list.insert(tk.END, f"{title} - {copies} copies")

def view_user_books_ui():
    name = user_name_entry.get()
    if name in library.users:
        user_books_list.delete(0, tk.END)
        for book in library.users[name]:
            user_books_list.insert(tk.END, book)
    else:
        messagebox.showerror("Error", f"User '{name}' is not registered.")

# Create Styled GUI
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x600")
root.configure(bg="#90e0ef")  

# Labels and Entries
tk.Label(root, text="Book Title:", bg="#f0f8ff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
book_title_entry = tk.Entry(root, font=("Arial", 10))
book_title_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Copies:", bg="#f0f8ff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
book_copies_entry = tk.Entry(root, font=("Arial", 10))
book_copies_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="User Name:", bg="#f0f8ff", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
user_name_entry = tk.Entry(root, font=("Arial", 10))
user_name_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons with Styling
tk.Button(root, text="Add Book", command=add_book_ui, bg="#4682b4", fg="white", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Delete Book", command=delete_book_ui, bg="#4682b4", fg="white", font=("Arial", 10)).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Register User", command=register_user_ui, bg="#228b22", fg="white", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="Borrow Book", command=borrow_book_ui, bg="#ffa07a", fg="white", font=("Arial", 10)).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Return Book", command=return_book_ui, bg="#ffa07a", fg="white", font=("Arial", 10)).grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="View Books", command=view_books_ui, bg="#9a031e", fg="white", font=("Arial", 10)).grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="View User's Books", command=view_user_books_ui, bg="#228b22", fg="white", font=("Arial", 10)).grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Listboxes with Styling
tk.Label(root, text="Books in Library:", bg="#f0f8ff", font=("Arial", 12)).grid(row=7, column=0, padx=10, pady=5)
books_list = tk.Listbox(root, height=10, width=50, font=("Arial", 10), bg="#f5f5f5", fg="#000")
books_list.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

tk.Label(root, text="User's Borrowed Books:", bg="#f0f8ff", font=("Arial", 12)).grid(row=9, column=0, padx=10, pady=5)
user_books_list = tk.Listbox(root, height=10, width=50, font=("Arial", 10), bg="#f5f5f5", fg="#000")
user_books_list.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

# Run the Application
root.mainloop()

# from library import load_books, save_books
# from user import load_users,save_users

# def borrow_book(user, title):
#     books = load_books()
#     users = load_users()

#     if title in books:
#         if user in users:
#             users


from library import load_books, save_books
from user import load_users, save_users

def borrow_book(user, title):
    books = load_books() 
    users = load_users()  

    if user in users:  
        if title in books:  
            if title not in users:

                ()
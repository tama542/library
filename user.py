import json

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

def register_user(name):
    users = load_users()
    users[name] = []
    save_users(users)
    print(f"User '{name}' registered.")

def view_users():
    users = load_users()
    print("Registered Users:")
    for user in users:
        print(user)

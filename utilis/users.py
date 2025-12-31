import csv
import os

USERS_FILE = os.path.join("Datas","users.csv")

def read_users():
    users= []

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(row)
            
    return users


def user_exists(username):
    users = read_users()
    for user in users:
        if user["username"] ==username:
            return True
        
    return False

def validate_login(username, password):
    users = read_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return user["role"]

    return None


def add_user(username, password, role):
    file_exists = os.path.exists(USERS_FILE)

    with open(USERS_FILE, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["username", "password", "role"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "username": username,
            "password": password,
            "role": role
        })
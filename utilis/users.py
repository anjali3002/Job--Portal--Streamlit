import csv
import os

USERS_FILE = os.path.join("Datas", "users.csv")

# ---------------- Read Users ----------------
def read_users():
    users = []

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(row)

    return users


# ---------------- Check Username ----------------
def user_exists(username):
    for user in read_users():
        if user["username"] == username:
            return True
    return False


# ---------------- Check Email ----------------
def email_exists(email):
    for user in read_users():
        if user.get("email") == email:
            return True
    return False


# ---------------- Validate Login ----------------
def validate_login(username, password):
    for user in read_users():
        if user["username"] == username and user["password"] == password:
            return user["role"]
    return None


# ---------------- Add User ----------------
def add_user(username, password, role, email, phone):
    file_exists = os.path.exists(USERS_FILE)

    with open(USERS_FILE, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["username", "password", "role", "email", "phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "username": username,
            "password": password,
            "role": role,
            "email": email,
            "phone": phone
        })


# ---------------- Get User Contact ----------------
def get_user_contact(username):
    if not os.path.exists(USERS_FILE):
        return None, None

    with open(USERS_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username:
                return row.get("email"), row.get("phone")

    return None, None

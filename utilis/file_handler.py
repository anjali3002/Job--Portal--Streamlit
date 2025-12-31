import csv
import os

USERS_FILE = os.path.join("Datas", "users.csv")

def read_users():
    users = []
    with open(USERS_FILE, mode='r', newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            clean_row = {}

            for k, v in row.items():
                if k is None:
                    continue
                clean_row[k] = v.strip() 

            users.append(clean_row)

    return users


def user_exists(username):
    users = read_users()
    for user in users:
        if user.get("username") == username:
            return True
    return False


def add_user(username, password, role):
    with open(USERS_FILE, mode='a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, role])

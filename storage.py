#This fuction will strore the password in the password in the passwords.json file.

import json

def save_a_password():
    with open("passwords.json", "r") as file:
        data = json.load(file)
        url = input("Website name(URL): ")
        username = input("Username: ")
        password = input("Password: ")
        password_info = {
            "Username": username,
            "Password": password
            }
        data[url] = password_info

        with open("passwords.json", "w") as file:
            json.dump(data, file, indent=4)


def retrieve_password():
    with open("passwords.json", "r") as file:
        data = json.load(file)
        url = input("Enter the URL of the password you are trying to find: ")
        if url in data:
            print(f"Username: {data[url]['Username']}")
            print(f"Password: {data[url]['Password']}")
        else:
            print("No password saved for this site")


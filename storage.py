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

def master_password():
    with open("master.json", "r") as file:
        data = json.load(file)
#If the length of data is 0 or there is nothing in the json file, I will have them create a username and passord and then write it to the file.
        while True:
            if len(data) == 0:
                print("Please create an account")
                create_username = input("Choose a username: ") 
                create_password = input("Choose a password: ")
                password_confirm = input("Confirm password: ")
                if create_password == password_confirm:
                    master_password = {
                        "Username": create_username,
                        "Password": password_confirm
                    }
                    data = master_password
                    with open("master.json", "w") as file:
                        json.dump(data, file, indent=4)
                else:
                    print("Please make sure your passwords match.")
                    break
            else:
                break


def sign_in():
    with open("master.json", "r") as file:
        data = json.load(file)
        while True:
            username = input("Username: ")
            master_password = input("Password: ")
            if username == data["Username"] and master_password == data["Password"]:
                break
            else:
                print("Your username or password are incorrect")


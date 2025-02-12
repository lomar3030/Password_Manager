#This fuction will strore the password in the password in the passwords.json file.

def save_a_password():
    import json
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

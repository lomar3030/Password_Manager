Password Manager

A simple password manager to store your passwords securely with a master password.
Features

    Store passwords for different websites or services
    Access your stored passwords with a master password

Installation

    Clone the repository:

git clone https://github.com/lomar3030/Password_Manager.git
cd Password_Manager

Install the required dependencies (if any):

    pip install -r requirements.txt

Usage

    Run the Password Manager:

    To run the password manager, execute the Python script:

    python password_manager.py

    Add a password:

    The script will prompt you to enter the website/service, username, and password. The information will be saved in the local files.

    View saved passwords:

    You can access the stored passwords by running the script and providing the master password.

Files in this repository

    password_manager.py: The main script to manage passwords.
    storage.py: Handles saving and loading the passwords.
    master.json: Stores password data (this file should not be tracked by Git and is ignored by .gitignore).
    passwords.json: Stores metadata for your passwords.

License

This project is licensed under the MIT License.

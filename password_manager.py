from utils import password_generator
from storage import save_a_password
from storage import retrieve_password
from storage import master_password
from storage import sign_in

master_password()
sign_in()

#Menu
while True:
    print("Welcome to Password Manager!")
    print("1. Generate a new password.")
    print("2. Save a password.")
    print("3. Retrieve a password.")
    print("4. Exit")
    menu_choice = int(input("Please choose the number for the option that you want: "))
    if menu_choice == 1:
        password_generator()
    elif menu_choice == 2:
        save_a_password()
    elif menu_choice == 3:
        retrieve_password()
    elif menu_choice == 4:
        print("Exiting now...\n")
        break
    else:
        print("Enter a valid option") 

from utils import password_generator
from storage import save_a_password

#Menu
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


import random

#This is a dictionary containing lists of the different characters that can be chosen for the password.
char_dict = {
    "Numbers": ["1", "2","3","4","5","6","7","8","9"],
    "Symbols": ["!","@","#","$","%","^","&","*"],
    "Lowercase": ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    "Uppercase": ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    }

def password_generator():
#This is the final list that the answers will go into.
    final_char_pool = []
    while True:
        include_numbers = input("Would you like to include numbers? y/n: ").lower().strip()
        if include_numbers == "y":
            final_char_pool.extend(char_dict["Numbers"])
        include_symbols = input("Include special symbols? y/n: ").lower().strip()
        if include_symbols == "y":
            final_char_pool.extend(char_dict["Symbols"])
        include_lowercase = input("Include lowercase letters? y/n: ").lower().strip()
        if include_lowercase == "y":
            final_char_pool.extend(char_dict["Lowercase"])
        include_uppercase = input("Include uppercase letters? y/n: ").lower().strip()
        if include_uppercase == "y":
            final_char_pool.extend(char_dict["Uppercase"])
#This is the final pool.
        if final_char_pool == []:
            print("Please select yes for at least one of the options.")

#I am taking the password length that the user enters and then printing randomly what the password is based on what characters they want to use.
        length = int(input("Enter password length: "))
        for i in range(length):
            print(random.choice(final_char_pool), end="")
        print()
        break


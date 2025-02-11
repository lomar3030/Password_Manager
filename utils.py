#I am taking the password length that the user enters and then printing randomly what the password is based on what characters they want to use.
def password_generator():
    length = int(input("Enter password length: "))
    for i in range(length):
        print(random.choice(final_char_pool), end="")
    print()


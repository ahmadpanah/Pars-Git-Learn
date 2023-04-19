import string
import random

charaters = list(string.ascii_letters + string.digits + "!@#$%^&*")

def generate_password():
    password_lenght = int(input("How Long Would you like your pass?"))

    random.shuffle(charaters)

    password = []

    for x in range(password_lenght):
        password.append(random.choice(charaters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a new password?")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Good Bye!")
    quit()
else:
    print("Invalid Option")
    quit()



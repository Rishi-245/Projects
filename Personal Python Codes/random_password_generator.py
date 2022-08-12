#Random Password Generator

import random
import string
import sys
import time

letters = list(string.ascii_letters)
numbers = list(string.digits)
special = ["!","@", "#","$", "%", "^", "&", "*", "(", ")", "-", "+", "="]
password_characters = list(letters + numbers + special)

def random_password():
    pass_length = eval(input("Enter the length of the password\n"))

    num_letters = eval(input("How many letters do you want in your password?\n"))
    num_numbers = eval(input("How many numbers do you want in your password?\n"))
    num_special = eval(input("How many special characters do you want in your password?\n"))

    num_total = num_letters + num_numbers + num_special

    if num_total > pass_length:
        print("The total number of characters is more than the number you want")
        sys.exit()

    generated_password = []

    if num_letters != 0:
        for i in range(num_letters):
            generated_password.append(random.choice(letters))


    if num_numbers != 0:
        for i in range(num_numbers):
            generated_password.append(random.choice(numbers))


    if num_special != 0:
        for i in range(num_special):
            generated_password.append(random.choice(special))


    if num_total < pass_length:
        print("The password length is more than the total characters you entered")

        time.sleep(1)

        user = input("Do you want to continue or no? y or n?\n").lower()

        if user == "y":
            random.shuffle(password_characters)

            for i in range(pass_length - num_total):
                generated_password.append(random.choice(password_characters))

            print("".join(generated_password))

        else:
            sys.exit()

    random.shuffle(password_characters)

    for i in range(pass_length - num_total):
        generated_password.append(random.choice(password_characters))

    print("".join(generated_password))
    

random_password()

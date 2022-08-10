import string
import random

alpha_characters = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("~!@#$%^&*")
all_characters = list(string.ascii_letters + string.digits + "~!@#$%^&*")


def generate_password():
    length = int(input("Total Number of Characters: "))

    alpha_char_count = int(input("Number of letters in password: "))
    digits_count = int(input("Number of numbers in password: "))
    special_char_count = int(input("Number of special characters in password: "))
    password_gen_count = int(input("Number of passwords you would like to generate: "))

    total_char_count = alpha_char_count + digits_count + special_char_count

    if total_char_count > length:
        print("Character total count is greater than password length")
    elif total_char_count < length:
        print("Character total count is less than password length.")

    password = []

    for i in range(password_gen_count):
        for x in range(alpha_char_count):
            password.append(random.choice(alpha_characters))
        for x in range(digits_count):
            password.append(random.choice(digits))
        for x in range(special_char_count):
            password.append(random.choice(special_characters))
        if total_char_count < length:
            random.shuffle(all_characters)
            for x in range(length - total_char_count):
                password.append(random.choice(all_characters))

        random.shuffle(password)

        print("".join(password))

        password = []


generate_password()

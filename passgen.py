import string
import random

alpha_characters_up = list(string.ascii_uppercase)
alpha_characters_lo = list(string.ascii_lowercase)
numbers = list(string.digits)
special_characters = list(string.punctuation)
all_characters = list(string.ascii_letters + string.digits + string.punctuation)


def generate_password():

    password_gen_count = int(input("Number of passwords you would like to generate: "))

    alpha_char_count_lo = int(input("Number of lower case letters in password: "))
    alpha_char_count_up = int(input("Number of UPPER case letter in password: "))
    number_count = int(input("Number of numbers in password: "))
    special_count = int(input("Number of special characters in password: "))

    password = []
    password_list = []

    for n in range(password_gen_count):
        for i in range(alpha_char_count_up):
            password.append(random.choice(alpha_characters_up))
        for i in range(alpha_char_count_lo):
            password.append(random.choice(alpha_characters_lo))
        for i in range(number_count):
            password.append(random.choice(numbers))
        for i in range(special_count):
            password.append(random.choice(special_characters))

        random.shuffle(password)
        password_string = "".join(password)
        password_list.append(password_string)

        password = []
    
    return password_list


test_list = generate_password()

for i in test_list:
    print(i)

print('\nList Length: ')
print(len(test_list))

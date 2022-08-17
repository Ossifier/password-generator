import string
import secrets
from random import shuffle

alpha_characters_up = list(string.ascii_uppercase)
alpha_characters_lo = list(string.ascii_lowercase)
numbers = list(string.digits)
special_characters = list(string.punctuation)
all_characters = list(string.ascii_letters + string.digits + string.punctuation)


def generate_passwords():
    password_gen_count = int(input("Number of passwords you would like to generate: "))

    alpha_char_count_lo = int(input("Number of lower case letters in password: "))
    alpha_char_count_up = int(input("Number of UPPER case letter in password: "))
    number_count = int(input("Number of numbers in password: "))
    special_count = int(input("Number of special characters in password: "))
    print('')

    password = []
    password_list = []

    for n in range(password_gen_count):
        for i in range(alpha_char_count_up):
            password.append(secrets.choice(alpha_characters_up))
        for i in range(alpha_char_count_lo):
            password.append(secrets.choice(alpha_characters_lo))
        for i in range(number_count):
            password.append(secrets.choice(numbers))
        for i in range(special_count):
            password.append(secrets.choice(special_characters))

        shuffle(password)
        password_string = "".join(password)
        password_list.append(password_string)

        password = []

    return password_list


def create_txt_dump(password_list):
    with open('passwords.txt', 'w') as f:
        f.write('***Passwords***\n\n')
        for password in password_list:
            f.write("%s\n" % password)
        print('')
        print('List Dump Complete.')


def retrieve_txt_dump():
    fresh_test_list = []
    list_from_file = open('passwords.txt', 'r').readlines()
    del list_from_file[:2]

    for i in list_from_file:
        fresh_test_list.append(i.strip())
    return fresh_test_list


if __name__ == '__main__':

    print('Run Directly, For Testing Purposes:\n')

    test_list = generate_passwords()

    for i in test_list:
        print(i)

    print('\nList Length: ')
    print(len(test_list))

    create_txt_dump(test_list)

    final_test_list = retrieve_txt_dump()

    print(list(final_test_list))

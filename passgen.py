import string
import secrets
from random import shuffle

alpha_characters_up = list(string.ascii_uppercase)
alpha_characters_lo = list(string.ascii_lowercase)
numbers = list(string.digits)
special_characters = list(string.punctuation)
all_characters = list(string.ascii_letters + string.digits + string.punctuation)


def generate_passwords_auto():
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
        password_string = ''.join(password)
        password_list.append(password_string)

        password = []

    return password_list


def create_txt_dump(password_list):
    with open('passwords.txt', 'w') as file:
        file.write('***Passwords***\n\n')
        for password in password_list:
            file.write("%s\n" % password)
        print('')
        print('List Dump Complete.')


def retrieve_txt_dump():
    fresh_text_list = []
    list_from_file = open('passwords.txt', 'r').readlines()
    del list_from_file[:2]

    for i in list_from_file:
        fresh_text_list.append(i.strip())
    return fresh_text_list


def trim_passwords(password_list):
    complete = False
    character_trim_list = []
    character_trim_string = ''
    new_list = []

    while complete is False:

        new_trim_chars = input('Please enter the characters you would like to trim: ')

        for i in new_trim_chars:
            if i in character_trim_list:
                pass
            else:
                character_trim_list.append(i)

            character_trim_string = ''.join(character_trim_list)

        quit_val = input('Would you like to add more characters? Y/N?: ').upper()

        if quit_val == 'Y':
            pass
        elif quit_val == 'N':
            complete = True
        else:
            print('Unexpected Error Detected...')

    for password_string in password_list:
        for character in character_trim_string:
            if character in password_string:
                new_string = password_string.replace(character, '')
                password_string = new_string
            else:
                pass
        new_list.append(password_string)
    return new_list


if __name__ == '__main__':

    print('Run Directly, For Testing Purposes:\n')

    test_list = generate_passwords_auto()

    for i in test_list:
        print(i)

    print('\nList Length: ')
    print(len(test_list))

    create_txt_dump(test_list)

    second_test_list = retrieve_txt_dump()

    trimmed_test_list = trim_passwords(second_test_list)

    create_txt_dump(trimmed_test_list)

    for i in trimmed_test_list:
        print(i)

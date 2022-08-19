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
        print('')


def retrieve_txt_dump():
    fresh_text_list = []
    list_from_file = open('passwords.txt', 'r').readlines()
    del list_from_file[:2]

    for i in list_from_file:
        fresh_text_list.append(i.strip())
    return fresh_text_list


def trim_passwords(password_list):
    character_trim_list = []
    character_trim_string = ''
    new_list = []

    new_trim_chars = input('Please enter the characters you would like to trim from your passwords: ')

    for c in new_trim_chars:
        if c in character_trim_list:
            pass
        else:
            character_trim_list.append(c)
        character_trim_string = ''.join(character_trim_list)

    for password_string in password_list:
        for c in character_trim_string:
            if c in password_string:
                new_string = password_string.replace(c, '')
                password_string = new_string
            else:
                pass
        new_list.append(password_string)
    return new_list


def spice_passwords(password_list):
    character_spice_list = []
    character_spice_string = ''
    new_list = []

    new_spice_chars = input('Please enter the characters you would like to spice your passwords with: ')

    for c in new_spice_chars:
        if c in character_spice_list:
            pass
        else:
            character_spice_list.append(c)
        character_spice_string = ''.join(character_spice_list)

    for password_string in password_list:
        for c in character_spice_string:
            if c not in password_string:
                new_string = (password_string + c)
                password_string = new_string
            else:
                pass

            l = list(password_string)
            shuffle(l)
            password_string = ''.join(l)

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
    print('')

    third_test_list = retrieve_txt_dump()
    
    spiced_test_list = spice_passwords(third_test_list)

    create_txt_dump(spiced_test_list)

    for i in spiced_test_list:
        print(i)
    print()

import os
import json


def get_folder_name():
    en_folder_name = input('Enter a folder name: ') + '/'
    print('Folder name: ' + en_folder_name)
    return en_folder_name


def get_file_name(folder):
    print('Directory Location ' + folder)
    en_file_name = input('Enter a file name: ') + '.json'
    print('File name: ' + en_file_name)
    return folder + en_file_name


def create_file(file):
    with open(file, 'x') as n_file:
        json.dump({}, n_file)


def create_folder(folder):
    os.makedirs(folder)


def load_file(file):
    with open(file, 'r') as l_file:
        loaded_file = json.load(l_file)
        return loaded_file


def file_check(password_folder, password_file):

    if os.path.exists(password_folder) is True:
        print('Folder exists.')

        if os.path.exists(password_file) is True:
            print('File exists.')
            load_file(password_file)

        else:
            print('File does not exist...')
            create_file(password_file)
            print('New file created.')
            load_file(password_file)

    else:
        print('Folder does not exist...')
        create_folder(password_folder)
        print('New folder created.')
        create_file(password_file)
        print('New file created.')
        load_file(password_file)


def get_user_info(password_file):

    file_data = load_file(password_file)
    length = len(file_data)

    en_name = input('Please enter a name for this login: ')
    print('You entered: ' + en_name)
    en_username = input('Please enter your username for this login if applicable: ')
    print('You entered: ' + en_username)
    en_email = input('Please enter an e-mail for this login if applicable: ')
    print('You entered: ' + en_email)
    en_password = input('Please enter a password for this login: ')
    print('You entered: ' + en_password)

    user_info = {length + 1: {"name": en_name, "username": en_username, "email": en_email, "password": en_password}}

    return user_info


def write_data(new_data, password_file):
    with open(password_file, 'r+') as file:
        file_data = json.load(file)
        file_data.update(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


folder_path = get_folder_name()
print(folder_path)
file_path = get_file_name(folder_path)
print(file_path)

file_check(folder_path, file_path)
enter_data = get_user_info(file_path)
write_data(enter_data, file_path)

print(load_file(file_path))

import json
import os


###>>>..................<<<###
### FOLDER & FILE HANDLERS ###
###>>>.................<<<####


def get_folder_name():
    en_folder_name = input('Enter a folder name: ') + '/'
    print('Folder name: ' + en_folder_name)
    return en_folder_name


def get_file_name(folder):
    print('Directory Location: ' + folder)
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


def check_for_file(password_folder, password_file):

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


def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)
        print(file + ' has been deleted!')
    else:
        print(file + ' does not exist.')


def delete_folder(folder):
    if os.path.isdir(folder):
        for file in os.scandir(folder):
            os.remove(file.path)
        os.rmdir(folder)
        print(folder + ' has been deleted!')
    else:
        print(folder + ' does not exist.')


###>>>...........................<<<###
### DATA READING & WRITING HANDLERS ###
###>>>..........................<<<####


def get_user_info():

    en_name = input('Please enter an index name for this login: ')
    print('You entered: ' + en_name)
    en_username = input('Please enter your username for this login if applicable: ')
    print('You entered: ' + en_username)
    en_email = input('Please enter an e-mail for this login if applicable: ')
    print('You entered: ' + en_email)
    en_password = input('Please enter a password for this login: ')
    print('You entered: ' + en_password)

    user_info = {en_name: {'username': en_username, 'email': en_email, 'password': en_password}}

    return user_info


def append_new_data(new_data, file_path):
    with open(file_path, 'r+') as file:
        file_data = json.load(file)
        file_data.update(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def add_json_entry():
    user_data = get_user_info()
    append_new_data(user_data, file_path)


def delete_entry(file_path):
    loaded_file = load_file(file_path)

    print('List of Passwords:\n')
    for key in loaded_file:
        print(key)
    print('')

    key_to_delete = input('Enter the name of the entry you would like to delete: ')
    print('')

    for key in loaded_file:
        if str(key) == str(key_to_delete):
            del loaded_file[key_to_delete]
            break
        else:
            pass

    with open(file_path, 'w+') as file:
        json.dump(loaded_file, file, indent=4)

    print('Key Deleted Successfully: ' + key_to_delete + '\n')


###>>>.......................<<<###
### FUNCTION TESTING SUBSECTION ###
###>>>......................<<<####


if __name__ == '__main__':

    print('Run Directly, For Testing Purposes:\n')

    folder_path = 'password-folder/'
    print(folder_path)
    file_path = 'password-folder/password-file.json'
    print(file_path)

    check_for_file(folder_path, file_path)

    continue_add = 'Y'
    while continue_add == 'Y':
        add_json_entry()
        continue_add = input('Do you want to add another entry? (Y/N): ')

    print('')

    continue_del = 'Y'
    while continue_del == 'Y':
        delete_entry(file_path)
        continue_del = input('Do you want to delete another entry? (Y/N): ')

    user_file_del = input('Delete File: (Y/N): ').upper()
    if user_file_del == 'Y':
        delete_file(file_path)
    else:
        pass

    user_fol_del = input('Delete Folder: (Y/N): ').upper()
    if user_fol_del == 'Y':
        dbl_check = input('WARNING! This will delete all files currently in this folder. Continue? (Y/N): ')
        if dbl_check == 'Y':
            delete_folder(folder_path)
        else:
            print('Operation Aborted.\n')
    else:
        pass

    print('\nOperations Complete.')

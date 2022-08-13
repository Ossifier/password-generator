import os
import json


folder_path = 'p_fldr_x/'
folder_exists = os.path.exists(folder_path)
file_path = 'p_fldr_x/pswds.json'
file_exists = os.path.exists(file_path)
new_entry = {}

def file_check():
    
    # Checks to see if folders/files exist. If they do not, then it generates them for you.
    # Consider using variables for filename directories in the future.

    if os.path.exists('p_fldr_x/') is True:
        print('Folder exists.')
        
        if os.path.exists('p_fldr_x/pswds.json') is True:
            print('File exists.')
            with open('p_fldr_x/pswds.json', 'r') as r_file:
                loaded_file = json.load(r_file)
                return loaded_file

        else:
            print('File does not exist...')
            with open('p_fldr_x/pswds.json', 'x') as new_json:
                json.dump({}, new_json)
                print('New file created.')
            with open('p_fldr_x/pswds.json', 'r') as r_file:
                loaded_file = json.load(r_file)
                return loaded_file

    else:
        print('Folder does not exist...')
        os.makedirs('p_fldr_x')
        print('Folder created.')
        with open('p_fldr_x/pswds.json', 'x') as new_json:
            json.dump({}, new_json)
            print('New file created.')
        with open('p_fldr_x/pswds.json', 'r') as r_file:
            loaded_file = json.load(r_file)
            return loaded_file
       
def get_user_info():
    with open('p_fldr_x/pswds.json', 'r') as file:
        file_data = json.load(file)
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
    print(user_info)

    return user_info


def write_password(new_data, filename='p_fldr_x/pswds.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data.update(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


file_check()

enter_data = get_user_info()
write_password(enter_data)


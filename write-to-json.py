import os
import json


folder_path = 'p_fldr_x/'
folder_exists = os.path.exists(folder_path)
file_path = 'p_fldr_x/pswds.json'
file_exists = os.path.exists(file_path)
new_entry = {}


if folder_exists is True:
    print('Folder exists.')
    if file_exists is True:
        print('File exists.')
        with open(file_path, 'r') as r_file:
            loaded_file = json.load(r_file)
    else:
        print('File does not exist...')
        with open(file_path, 'x') as new_json:
            json.dump({}, new_json)
            print('New file created.')
        with open(file_path, 'r') as r_file:
            loaded_file = json.load(r_file)
            
else:
    print('Folder does not exist...')
    os.makedirs('p_fldr_x')
    print('Folder created.')
    with open(file_path, 'x') as new_json:
        json.dump({}, new_json)
        print('New file created.')
    with open(file_path, 'r') as r_file:
        loaded_file = json.load(r_file)

print('')

def add_entry():
        name = input('Please enter a name for this login: ')
        print('You entered: ' + name)
        user = input('Please enter your username for this login if applicable: ')
        print('You entered: ' + user)
        em = input('Please enter an e-mail for this login if applicable: ')
        print('You entered: ' + em)
        password_en = input('Please enter a password for this login: ')
        print('You entered: ' + password_en)

        dict_length = len(loaded_file)

        new_entry[dict_length + 1] = {'name': name, 'username': user, 'e-mail': em, 'password': password_en}

        json_object = json.dumps(new_entry, indent=4)
        print(json_object)

        with open(file_path, 'w+') as add_new:
            add_new.write(json_object)


add_entry()

import passgen as pg
import writejson as wj

###>>>    ,------.                       ,--. ,--.  ,--.  ,--.,--.    <<<###
###>>>    |  .--. ' ,--,--. ,---.  ,---. |  | |  |,-'  '-.`--'|  |    <<<###
###>>>    |  '--' |' ,-.  |(  .-' (  .-' |  | |  |'-.  .-',--.|  |    <<<###
###>>>    |  | --' \ '-'  |.-'  `).-'  `)'  '-'  '  |  |  |  ||  |    <<<###
###>>>    `--'      `--`--'`----' `----'  `-----'   `--'  `--'`--'    <<<###

if __name__ == '__main__':
    quit_util = False
    print('\n☆ﾟ.*･｡ﾟ  ~Welcome to PassUtil~  ☆ﾟ.*･｡ﾟ\n')

    print('Type \'help\' and hit Enter for the full command list.')

    txt_folder_path = ''
    txt_file_path = ''
    json_folder_path = ''
    json_file_path = ''
    
    while quit_util is False:
        user_command = input('\nCast your magic spell: ☆ﾟ.*･｡ﾟ ')
        print('')

        if user_command == 'help':
            print('\n☆ﾟ.*･｡ﾟCommand List☆ﾟ.*･｡ﾟ\n')
            print('>>> gen p ---> Creates a new password list and dumps that list to a .txt file.')
            print('>>> pt all p ---> Prints all the passwords from .txt file.')
            print('>>> get p by ind ---> Prints the passwords from .txt file within a user-specified range.')
            print('>>> w json ---> Writes data to .json files, also allows user to create new files and directories.')
            print('>>> get dir ---> Gets a directory name for managing your working directory.')
            print('>>> mk dir ---> Creates a new directory.')
            print('>>> json name ---> Gets a file name for creating files and retrieving file data.')
            print('>>> quit ---> Quits the program.\n')

        if user_command == 'gen p':
            new_password_list = pg.generate_passwords_auto()
            txt_file_name = input('Please enter a name for your new file: ') + '.txt'
            pg.create_txt_dump(new_password_list, txt_file_name)

        if user_command == 'pt all p':
            txt_file_path = input('Please enter your password filename. ') + '.txt'
            print(txt_file_path + '\n')
            retrieved_list = pg.retrieve_txt_dump(txt_file_path)
            for st in retrieved_list:
                print(st)

        if user_command == 'get pswds by ind':
            txt_file_name = input('Please enter your file name: ') + '.txt'
            retrieved_list = pg.retrieve_txt_dump(txt_file_name)
            pg.retrieve_password_by_index(retrieved_list)

        if user_command == 'w json':
            if json_folder_path == '':
                json_folder_path = wj.get_folder_name()
            if json_file_path == '':
                json_file_path = wj.get_file_name(json_folder_path)
            print('\nFile Path: ' + json_file_path + '\n')

            wj.check_for_file(json_folder_path, json_file_path)

            quit_add = True
            while quit_add is True:
                add_new = input('Would you like to add entries? (Y/N): ').upper()
                if add_new == 'Y':
                    wj.add_json_entry(json_file_path)
                elif add_new == 'N':
                    quit_add = False
                else:
                    print('Command not recognized. Please enter Y for yes, or N for no.')

        if user_command == 'get dir':
            json_folder_path = wj.get_folder_name()

        if user_command == 'mk dir':
            wj.create_folder(json_folder_path)
            print('')

        if user_command == 'json name':
            json_folder_path = wj.get_folder_name()
            json_file_path = wj.get_file_name(json_folder_path)

        if user_command == 'quit':
            quit_util = True
            
    print('Goodbye!')
    

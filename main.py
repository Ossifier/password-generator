import passgen as pg
import writejson as wj

###>>>    ,------.                       ,--. ,--.  ,--.  ,--.,--.    <<<###
###>>>    |  .--. ' ,--,--. ,---.  ,---. |  | |  |,-'  '-.`--'|  |    <<<###
###>>>    |  '--' |' ,-.  |(  .-' (  .-' |  | |  |'-.  .-',--.|  |    <<<###
###>>>    |  | --' \ '-'  |.-'  `).-'  `)'  '-'  '  |  |  |  ||  |    <<<###
###>>>    `--'      `--`--'`----' `----'  `-----'   `--'  `--'`--'    <<<###


if __name__ == '__main__':
    quit_util = False

    print('\n☆ﾟ.*･｡ﾟ  !Welcome to PassUtil!  ☆ﾟ.*･｡ﾟ\n')

    print('Type \'help\' and hit Enter for the full command list.\n')

    folder_path = ''
    file_path = ''

    while quit_util is False:
        print('')
        user_command = input('Cast your magic spell: ☆ﾟ.*･｡ﾟ ')
        print('')

        if user_command == 'help':
            print('\n☆ﾟ.*･｡ﾟCommand List☆ﾟ.*･｡ﾟ\n')
            print('>>> gen pswds ---> Creates a new password list and dumps that list to a .txt file.')
            print('>>> pt pswds ---> Prints the passwords from the password list you have generated.')
            print('>>> w json ---> Writes data to .json file. If a file does not exist, prompts for a file/folder name and creates it.')
            print('>>> dir name ---> Gets a directory name for managing folders.')
            print('>>> mk dir ---> Creates a new directory based on the dir name.')
            print('>>> file name ---> Gets a file name for creating files and retrieving file data.')
            print('>>> get pswds list ---> Retrieves and prints a password from your randomly generated .txt file.')
            print('>>> quit ---> Quits the program.\n')

        if user_command == 'gen pswds':
            new_password_list = pg.generate_passwords_auto()
            txt_file_name = input('Please enter a name for your new file: ') + '.txt'
            pg.create_txt_dump(new_password_list, txt_file_name)

        if user_command == 'pt all pswds':
            file_path = input('Please enter your password filename. ') + '.txt'
            print(file_path + '\n')
            retrieved_list = pg.retrieve_txt_dump(file_path)
            for st in retrieved_list:
                print(st)
            print('')

        if user_command == 'w json':
            if folder_path == '':
                folder_path = wj.get_folder_name()
            if file_path == '':
                file_path = wj.get_file_name(folder_path)
            print('\nFile Path: ' + file_path + '\n')

            wj.check_for_file(folder_path, file_path)
            
            quit_add = True
            while quit_add == True:
                add_new = input('Would you like to add entries? (Y/N): ').upper()
                if add_new == 'Y':
                    wj.add_json_entry(file_path)
                elif add_new == 'N':
                    quit_add = False
                else:
                    print('Command not recognized. Please enter Y for yes, or N for no.')



        if user_command == 'dir name':
            folder_path = wj.get_folder_name()

        if user_command == 'mk dir':
            wj.create_folder(folder_path)
            print('')

        if user_command == 'file name':
            folder_path = wj.get_folder_name()
            file_path = wj.get_file_name(folder_path)

        if user_command == 'get pswds list':
            txt_file_name = input('Please enter your file name: ') + '.txt'
            retrieved_list = pg.retrieve_txt_dump(txt_file_name)
            pg.retrieve_password_by_index(retrieved_list)
            print('')

        if user_command == 'quit':
            quit_util = True

    print('Goodbye!')
    

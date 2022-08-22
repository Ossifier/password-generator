import os
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

        user_command = input('Cast your magic spell. ༼༼(ಠ ╭͜ʖ╮ಠ)༽༽⊃ ━━ ☆ﾟ.*･｡ﾟ ')

        if user_command == 'gen pswds':
            new_password_list = pg.generate_passwords_auto()
            txt_file_name = input('Please enter a name for your new file: ') + '.txt'
            pg.create_txt_dump(new_password_list, txt_file_name)

        if user_command == 'mk json':
            if folder_path == '':
                folder_path = wj.get_folder_name()
            if file_path == '':
                file_path = wj.get_file_name(folder_path)
            print('\nFile Path: ' + file_path + '\n')
            wj.check_for_file(folder_path, file_path)

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

        if user_command == 'help':
            print('\n☆ﾟ.*･｡ﾟCommand List☆ﾟ.*･｡ﾟ\n')
            print('>>> gen pswds ---> Creates a new password list and dumps that list to a .txt file.')
            print('>>> mk json ---> Creates new .json data file. Prompts for file/folder name if none exists.')
            print('>>> dir name ---> Gets a directory name for managing folders.')
            print('>>> mk dir ---> Creates a new directory based on the dir name.)
            print('>>> file name ---> Gets a file name for creating files and retrieving file data.')
            print('>>> get pswds list ---> Retrieves and prints a password from your randomly generated .txt file.')
            print('>>> quit ---> Quits the program.\n')

        if user_command == 'quit':
            quit_util = True

        #print('Command does not exist. Type \'help\' to return the full command list.\n')

    print('\nGoodbye!')

import passgen as pg
import writejson as wj

###>>>    ,------.                       ,--. ,--.  ,--.  ,--.,--.    <<<###
###>>>    |  .--. ' ,--,--. ,---.  ,---. |  | |  |,-'  '-.`--'|  |    <<<###
###>>>    |  '--' |' ,-.  |(  .-' (  .-' |  | |  |'-.  .-',--.|  |    <<<###
###>>>    |  | --' \ '-'  |.-'  `).-'  `)'  '-'  '  |  |  |  ||  |    <<<###
###>>>    `--'      `--`--'`----' `----'  `-----'   `--'  `--'`--'    <<<###

print('\n☆ﾟ.*･｡ﾟ  !Welcome to PassUtil!  ☆ﾟ.*･｡ﾟ\n')


if __name__ == '__main__':
    quit_util = False
    print('☆ﾟ.*･｡ﾟCommand List☆ﾟ.*･｡ﾟ\n')
    print('>>> new ps txt ---> Creates a new password list and dumps that list to a .txt file.')
    print('>>> new ps json ---> Creates new directory and .json file for password storage.')
    print('>>> get ps txt ---> Retrieves and prints a password from your randomly generated .txt file.')
    print('>>> quit ---> Quits the program.')
    print('')

    while quit_util is False:

        user_command = input('My Wish is Your Command! ༼༼(ಠ ╭͜ʖ╮ಠ)༽༽⊃ ━━ ☆ﾟ.*･｡ﾟ ')

        if user_command == 'new ps txt':
            new_password_list = pg.generate_passwords_auto()
            txt_file_name = input('Please enter a name for your new file: ') + '.txt'
            pg.create_txt_dump(new_password_list, txt_file_name)

        if user_command == 'new ps json':
            folder_path = wj.get_folder_name()
            file_path = wj.get_file_name(folder_path)
            print(folder_path)
            print(file_path)
            wj.file_check(folder_path, file_path)

        if user_command == 'get ps txt':
            txt_file_name = input('Please enter your file name: ') + '.txt'
            retrieved_list = pg.retrieve_txt_dump(txt_file_name)
            pg.retrieve_password_by_index(retrieved_list)
            print('')

        if user_command == 'quit':
            quit_util = True

    print('Goodbye!')

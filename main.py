import datetime
import os

def add_info_user():
    pass


def user_registration():
    while True:
        nickname = input("фио: ")
        nickname = nickname.split(" ")
        nick_user = nickname[-1]
        path = f'./users/{nick_user}.txt'
        dirs = os.path.exists(path)
        if dirs != True:
            break
    gender = input("пол: ")
    date_birth = input("дата: ")
    email = input("email: ")
    password = input("пароль: ")




    date = date_birth.split('.')
    age = str((datetime.datetime.now() - datetime.datetime(int(date[2]), int(date[1]), int(date[0]))) / 365.2425)
    age = age[:2]

    users = [nickname, gender, date_birth, age, "", "", "", False, email, password, ["", [], [], True, "", ""]]

    num = 0
    while num < 11:
        with open(f"./users/{nick_user}.txt", "a", encoding='utf8') as user:
            user.write(f"\n{users[num]}")
        num += 1

    return nick_user

def main():
    user_registration()
    # add_info_user()

    # with open("./users/yes.txt", "r" ,encoding='utf8') as file:
    #     files = file.read()
    #     files = files.replace("\n", "•").split('•')
    #     print(files)
    # files[5] = "Жопа"
    # print(files)
    # files[5] = ""
    # print(files)

    # path = './users/'
    # print(os.listdir(path))

    # file_name = os.path.exists(f'./users/yes_1.txt')
    # print(file_name)

if __name__ == '__main__':
    main()

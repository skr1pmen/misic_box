import datetime
import time
import os
import re
import edit_user as edit_u


def add_music(active_user):
    user_data = edit_u.get_file(active_user)
    is_admin = int(user_data[8])
    if is_admin != 1:
        print("Нет прав!")
        return
    musics = os.listdir('./musics/')
    id = str(len(musics))
    name = input("Введите название песни: ")
    tags = input("Введите теги, если их много, то укажите через запятую: ")
    author = input("Введите автора: ")
    musuc_len = input("Введите длинну песни: ")
    music_url = input("Введите ссылку на песню: ")

    tags = tags.split(", ")

    music_info = [id, name, tags, [author, musuc_len, music_url]]
    num = 0
    while num < len(music_info):
        with open(f"./musics/{name}.txt", "a", encoding="utf8") as music:
            music.write(f"\n{music_info[num]}")
        num += 1


def edit_user_info(active_user):
    """Небольшая шпаргалка позиции данных в файле:
    1 - Пустая игнорируемая строка;
    2 - ФИО и Никнейм пользователя (список/массив);
    3 - Пол пользователя (строка);
    4 - Дата рождения пользователя (строка);
    5 - Возраст пользователя (строка);
    6 - Национальность пользователя (строка);
    7 - Профессии пользователя (список/массив);
    8 - Хобби/Увлечения пользователя (список/массив);
    9 - Является ли пользователем Администратором (bool);
    10 - Email пользователя (строка);
    11 - Пароль пользователя (строка);
    12 - Плейлисты пользователя (список/массив);
        0 Элемент в массиве:
        12.1 - Название плейлиста("Моя музыка") (строка);
        12.2 - Теги всех песен в плейлисте (список/массив);
        12.3 - ID музыки (список/массив);
        12.4 - Рейтинг/Релевантность музыки (bool);
        12.5 - Количество песен в плейлисте (строка);
        12.6 - Длинна всех песен в плейлисте (строка);
    """
    result = edit_u.nationality(active_user)
    result = edit_u.profession(active_user)
    result = edit_u.hobby(active_user)
    print(result)


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
    users_dir = os.listdir('./users/')
    emails = []
    for item in users_dir:
        item = item[:-4]
        user_data = edit_u.get_file(item)
        emails.append(user_data[9][:-1])
    while True:
        email = input("email: ")
        if email in emails:
            print("Пароль занят, попробуй ещё раз!")
            continue
        else:
            break
    password = input("пароль: ")

    date = date_birth.split('.')
    age = str((datetime.datetime.now() - datetime.datetime(int(date[2]), int(date[1]), int(date[0]))) / 365.2425)
    age = age[:2]

    users = [nickname, gender, date_birth, age, "", [], [], 0, email, password, "", "Моя музыка", [], [], True, 0, "00:00:00"]
    num = 0
    while num < len(users):
        with open(f"./users/{nick_user}.txt", "a", encoding='utf8') as user:
            user.write(f"\n{users[num]}")
        num += 1

    return nick_user


def show_music():
    filter = input("Категория песен: ")
    all_music = os.listdir("./musics/")
    print("Список доступных песен: ")
    if filter == '':
        for music in all_music:
            with open(f"./musics/{music}", "r", encoding="utf8") as file:
                music_info = file.readlines()
                id = music_info[1][:-1]
                name = music_info[2][:-1]
                tags = re.sub(r'[\n\[\]\']', '', music_info[3]).split(',')
                info = re.sub(r'[\n\[\]\']', '', music_info[4])
                print(f'\t{id} | {name} : {info}')
    else:
        for music in all_music:
            with open(f"./musics/{music}", "r", encoding="utf8") as file:
                music_info = file.readlines()
                id = music_info[1][:-1]
                name = music_info[2][:-1]
                tags = re.sub(r'[\n\[\]\']', '', music_info[3]).split(',')
                info = re.sub(r'[\n\[\]\']', '', music_info[4])
                for tag in tags:
                    if filter in tag:
                        print(f'\t{id} | {name} : {info}')


def time_converter(time):
    time = time.split(":")
    if len(time) == 1:
        return int(time[-1])
    elif len(time) == 2:
        sec = int(time[-1])
        min = int(time[-2])
        return min * 60 + sec
    else:
        sec = int(time[-1])
        min = int(time[-2])
        hour = int(time[-3])
        return hour * 3600 + min * 60 + sec


def add_music_in_playlist(active_user):
    id = input("Введите id песни: ")
    music_list = os.listdir("./musics/")
    for music in music_list:
        with open(f"./musics/{music}", "r", encoding="utf8") as file:
            music_information = file.readlines()
            if id == music_information[1][:-1]:
                user = edit_u.get_file(active_user)
                playlist_tags = re.sub(r'[\n\[\]\']', '', user[13][:-1]).split(', ')
                playlist_id_music = re.sub(r'[\n\[\]\']', '', user[14][:-1]).split(', ')
                playlist_num = int(user[16][:-1])
                playlist_len = time_converter(user[17])

                music_id = list(music_information[1][:-1])
                music_tags = re.sub(r'[\n\[\]\']', '', music_information[3][:-1]).split(', ')
                music_info = re.sub(r'[\n\[\]\']', '', music_information[4]).split(', ')
                music_authors = list()
                i = 0
                while i < len(music_info) - 2:
                    music_authors.append(music_info[i])
                    i += 1
                music_len = time_converter(music_info[-2])

                playlist_tags = list(filter(None, set(playlist_tags + music_tags)))
                playlist_id_music = list(filter(None, set(playlist_id_music + music_id)))
                playlist_num += 1
                playlist_len += music_len
                format_time = time.strftime("%H:%M:%S", time.gmtime(playlist_len))

                user[13] = f"{playlist_tags}\n"
                user[14] = f"{playlist_id_music}\n"
                user[16] = f"{playlist_num}\n"
                user[17] = f"{format_time}"

                edit_u.set_file(active_user, user)


def login():
    all_users = os.listdir("./users/")
    for user_file in all_users:
        with open(f"./users/{user_file}", "r", encoding="utf8") as file:
            user_data = file.readlines()
            nick_user = user_file[:-4]
            user_email = user_data[9][:-1]
            user_password = user_data[10][:-1]
            while True:
                email = input("Введите emai: ").lower()
                if email == user_email:
                    password = input("Введите пароль: ").lower()
                    if password == user_password:
                        print("Успешная авторизация!")
                        return nick_user
                    else:
                        print("Неверный пароль, попробуй ещё раз!")
                else:
                    print("Неверная почта, попробуй ещё раз!")


def main():
    active_user = "skr1pmen"

    #  ↓ Активный пользователь программы, выбирается в Регистрации/Авторизации
    # active_user = login()  # Функция авторизации пользователей
    # active_user = user_registration()  # Функция регистрации пользователя
    # edit_user_info(active_user)  # Функция редактирования данных пользователя
    # add_music(active_user)  # Функция добавление музыки
    show_music()  # Функция просмотра всех песен в базе
    # add_music_in_playlist(active_user)  # Функция добавления песен в плейлист


if __name__ == '__main__':
    main()

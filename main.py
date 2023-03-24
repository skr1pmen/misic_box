import datetime
import time
import os
import re
import edit_user as edit_u


def add_music(active_user):
    user_data = edit_u.get_file(active_user)  # Получение всех данных пользователя
    is_admin = int(user_data[8])  # Запись в переменную свойство пользователя (админ или нет)
    if is_admin != 1:  # Проверка. 1 = Админ 2 = обычный пользователь
        print("Нет прав!")
        return  # Выход из функции если не админ
    musics = os.listdir('./musics/')  # Получение Списка всех песен в папке musics
    id = str(len(musics))  # Создание id для новой песни считая количество песен до этого
    name = input("Введите название песни: ")
    tags = input("Введите теги, если их много, то укажите через запятую: ")
    author = input("Введите автора: ")
    musuc_len = input("Введите длинну песни: ")
    music_url = input("Введите ссылку на песню: ")

    tags = tags.split(", ")  # Создание списка тегов из введённых данных

    music_info = [id, name, tags, [author, musuc_len, music_url]]  # Создание структуры записи данных в файл
    num = 0  # Счётчик для цикла
    while num < len(music_info):  # Цикл перебора всего переменной music_info
        with open(f"./musics/{name}.txt", "a", encoding="utf8") as music:  # Создание файла с названием песни в папке musics
            music.write(f"\n{music_info[num]}")  # Запись каждого элемента music_info на новую строчку
        num += 1  # Увеличиваем счётчик


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
    12 - Пустая игнорируемая строка;
    13 - Название плейлиста("Моя музыка") (строка);
    14 - Теги всех песен в плейлисте (список/массив);
    15 - ID музыки (список/массив);
    16 - Рейтинг/Релевантность музыки (bool);
    17 - Количество песен в плейлисте (строка);
    18 - Длинна всех песен в плейлисте (строка)."""

    edit_u.nationality(active_user)  # Функция добавление национальности пользователю
    edit_u.profession(active_user)  # Функция добавление профессий пользователю
    edit_u.hobby(active_user)  # Функция добавления хобби пользователю


def user_registration():
    while True:  # Создание бесконечного цикла
        nickname = input("фио: ")
        nickname = nickname.split(" ")  # Создание списка из данных пользователя
        nick_user = nickname[-1]  # Создание никнейма
        path = f'./users/{nick_user}.txt'  # Создание пути будущего файла
        dirs = os.path.exists(path)  # Проверка на существование файла
        if dirs != True:  # Проверка результата переменной dirs
            break  # Если файла нет, выход из бесконечного цикла
    gender = input("пол: ")
    date_birth = input("дата: ")
    users_dir = os.listdir('./users/')  # Создание списка всех файлов пользователей
    emails = []  # Создание пустого списка для электронных почт всех пользователей
    for item in users_dir:  # Цикл для перебора всех файлов
        item = item[:-4]  # Из названия файла убираем формат (.txt)
        user_data = edit_u.get_file(item)  # Получение всех данных пользователя
        emails.append(user_data[9][:-1])  # Добавление email в общий список почт
    while True:  # Создание бесконечного цикла
        email = input("email: ")
        if email in emails:  # Проверка данных от пользователя с списком всех почти других пользователей
            print("Пароль занят, попробуй ещё раз!")
            continue  # Если почта занята, то возвращаемся в начало цикла
        else:  # Блок иначе
            break  # Выход из цикла
    password = input("пароль: ")

    date = date_birth.split('.')  # Форматирование даты для дальнейшей валидации
    age = str((datetime.datetime.now() - datetime.datetime(int(date[2]), int(date[1]), int(date[0]))) / 365.2425)  # Получение примерного возраста пользователя
    age = age[:2]  # Из возраста вырезаем лишнее

    users = [nickname, gender, date_birth, age, "", [], [], 0, email, password, "", "Моя музыка", [], [], True, 0, "00:00:00"]  # Создание структуры записи данных в файл
    num = 0  # Счётчик для цикла
    while num < len(users):  # Цикл перебора данных из переменной users
        with open(f"./users/{nick_user}.txt", "a", encoding='utf8') as user:  # Создание файла с никнеймом пользователя в папке users
            user.write(f"\n{users[num]}")  # Запись каждого элемента users на новую строчку
        num += 1  # Увеличиваем счётчик

    return nick_user  # Возвращаем активного пользователя


def show_music():
    filter = input("Категория песен: ")
    all_music = os.listdir("./musics/")  # Создание списка всех файлов музыки
    print("Список доступных песен: ")
    for music in all_music:  # Цикл перебора списка all_music
        with open(f"./musics/{music}", "r", encoding="utf8") as file:  # Открытие файла с название music на чтение
            music_info = file.readlines()  # Создание массива данных песни
            id = music_info[1][:-1]  # Получение и сохранение id песни
            name = music_info[2][:-1]  # Получение и сохранение названия песни
            tags = re.sub(r'[\n\[\]\']', '', music_info[3]).split(',')  # Получение и сохранение тегов песни
            info = re.sub(r'[\n\[\]\']', '', music_info[4])  # Получение и сохранение остальных данных песни
            if filter != '':  # Условие если в фильтре что-то есть
                for tag in tags:  # Перебор всех тегов в песни
                    if filter in tag:  # Проверка есть ли фильтр в тегах песни
                        print(f'\t{id} | {name} : {info}')  # Вывод песен
            else:  # Блок иначе
                print(f'\t{id} | {name} : {info}')  # Вывод песен


def time_converter(time):
    time = time.split(":")  # Форматирование времени в нужный формат (в список)
    if len(time) == 1:  # Условия если в списке 1 элемент
        return int(time[-1])  # Возвращение времени переведённого в секунды
    elif len(time) == 2:  # Условия если в списке 2 элемента
        sec = int(time[-1])  # Получение и сохранение секунд
        min = int(time[-2])  # Получение и сохранение минут
        return min * 60 + sec  # Возвращение времени переведённого в секунды
    else:  # Блок иначе
        sec = int(time[-1])  # Получение и сохранение секунд
        min = int(time[-2])  # Получение и сохранение минут
        hour = int(time[-3])  # Получение и сохранение часов
        return hour * 3600 + min * 60 + sec  # Возвращение времени переведённого в секунды


def add_music_in_playlist(active_user):
    id = input("Введите id песни: ")
    music_list = os.listdir("./musics/")  # Создание списка всех файлов песен
    for music in music_list:  # Цикл перебора названий фалов музыки
        with open(f"./musics/{music}", "r", encoding="utf8") as file:  # Открытие файла на чтение
            music_information = file.readlines()  # Сохранение всех данных из файла
            if id == music_information[1][:-1]:  # Сравнение данных пользователя с информацией из файла
                user = edit_u.get_file(active_user)  # Получение всех данных пользователя
                playlist_tags = re.sub(r'[\n\[\]\']', '', user[13][:-1]).split(', ')  # Получение и сохранение тегов плейлиста
                playlist_id_music = re.sub(r'[\n\[\]\']', '', user[14][:-1]).split(', ')  # Получение и сохранение id песен в плейлисте
                playlist_num = int(user[16][:-1])  # Получение и сохранение количество песен в плейлисте
                playlist_len = time_converter(user[17])  # Получение и сохранение общей длительности песен в плейлисте

                music_id = list(music_information[1][:-1])  # Получение и сохранение id песни
                music_tags = re.sub(r'[\n\[\]\']', '', music_information[3][:-1]).split(', ')  # Получение и сохранение тегов песни
                music_info = re.sub(r'[\n\[\]\']', '', music_information[4]).split(', ')  # Получение и сохранение информации о песне
                music_authors = list()  # Создание пустого списка для авторов песни
                i = 0  # Счётчик для цикла
                while i < len(music_info) - 2:  # Цикл перебора информации о песне
                    music_authors.append(music_info[i])  # Добавление авторов в общий список
                    i += 1  # Увеличение счётчика
                music_len = time_converter(music_info[-2])  # Вызов функции для перевода времени в секунды

                playlist_tags = list(filter(None, set(playlist_tags + music_tags)))  # Изменение тегов плейлиста
                playlist_id_music = list(filter(None, set(playlist_id_music + music_id)))  # Изменение id песен в плейлисте
                playlist_num += 1  # Изменение количество песен в плейлисте
                playlist_len += music_len  # Изменение Общей длинны плейлиста
                format_time = time.strftime("%H:%M:%S", time.gmtime(playlist_len))  # Форматирование времени из секунд в нормальное время

                user[13] = f"{playlist_tags}\n"  # Перезапись тегов у пользователя
                user[14] = f"{playlist_id_music}\n"  # Перезапись id песен у пользователя
                user[16] = f"{playlist_num}\n"  # Перезапись количества песен у пользователя
                user[17] = f"{format_time}"  # Перезапись Общего времени песен у пользователя

                edit_u.set_file(active_user, user)  # Вызов функции для сохранения данных
            else:  # Блок иначе
                print("Песня не найдена!")


def login():
    all_users = os.listdir("./users/")  # Создание списка всех файлов пользователей
    for user_file in all_users:  # Цикл для перебора всех файлов
        with open(f"./users/{user_file}", "r", encoding="utf8") as file:  # Открытие файла на чтение
            user_data = file.readlines()  # Сохранение всех данных из файла
            nick_user = user_file[:-4]  # Получение и сохранение никнейма пользователя
            user_email = user_data[9][:-1]  # Получение и сохранение email пользователя
            user_password = user_data[10][:-1]  # Получение и сохранение пароля пользователя
            while True:  # Создание бесконечного цикла
                email = input("Введите emai: ").lower()  # Получение данных от пользователя и перевод в нижний регистр
                if email == user_email:  # Проверка на правильность email
                    password = input("Введите пароль: ").lower()  # Получение данных от пользователя и перевод в нижний регистр
                    if password == user_password:  # Проверка на правильность пароля
                        print("Успешная авторизация!")
                        return nick_user  # Возвращаем активного пользователя если всё получилось
                    else:  # Блок иначе
                        print("Неверный пароль, попробуй ещё раз!")
                else:  # Блок иначе
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

import os
import re
import edit_user as edit_u


def show_user_music(active_user):
    all_music = os.listdir("./musics/")  # Создание списка всех файлов музыки
    user_data = edit_u.get_file(active_user)  # Получение всех данных пользователя
    playlist_name = user_data[12][:-1]  # Название плейлиста
    playlist_tags = re.sub(r'[\n\[\]\']', '', user_data[13][:-1]).split(', ')  # Теги плейлиста
    playlist_music_id = re.sub(r'[\n\[\]\']', '', user_data[14][:-1]).split(', ')  # Id песен плейлиста
    playlist_num = user_data[16][:-1]  # Количество песен в плейлисте
    playlist_len = user_data[17]  # Общая длительность плейлиста

    result = []
    for id in playlist_music_id:
        for music in all_music:
            with open(f"./musics/{music}", "r", encoding="utf8") as file:  # Открытие файла с названием music на чтение
                music_info = file.readlines()  # Создание массива данных песни
                music_id = music_info[1][:-1]  # Получение и сохранение id песни
                music_name = music_info[2][:-1]  # Получение и сохранение названия песни
                music_tags = re.sub(r'[\n\[\]\']', '', music_info[3]).split(', ')  # Получение и сохранение тегов песни
                music_info = re.sub(r'[\n\[\]\']', '', music_info[4]).split(", ")  # Получение и сохранение остальных данных песни
                music_authors = music_info[0:-2]  # Получение авторов песни
                music_len = music_info[-2]  # Получение длинны песен
                music_link = music_info[-1]  # Получение ссылки на песню
                if id == music_id:
                    # Добавляем в общий список песен пользователя Id песни, Название песни, Авторов песни (список), Теги песни (список), Длинну песни, Ссылку на песню
                    result.append([music_id, music_name, music_authors, music_tags, music_len, music_link])

    # Возврат Названия плейлиста, Его тегов (список), Список песен (список), Количество песен в плейлисте, Общая длительность плейлиста и все песни пользователя
    return playlist_name, playlist_tags, playlist_music_id, playlist_num, playlist_len, result

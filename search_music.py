import os
import re
import time

import edit_user
import edit_user as edit_u
import main


def search_music(search_music):
    all_music = os.listdir("./musics/")  # Создание списка всех файлов музыки
    for music in all_music:  # Цикл перебора списка all_music
        with open(f"./musics/{music}", "r", encoding="utf8") as file:  # Открытие файла с названием music на чтение
            music_info = file.readlines()  # Создание массива данных песни
            id = music_info[1][:-1]  # Получение и сохранение id песни
            name = music_info[2][:-1]  # Получение и сохранение названия песни
            tags = re.sub(r'[\n\[\]\']', '', music_info[3]).split(',')  # Получение и сохранение тегов песни
            info = re.sub(r'[\n\[\]\']', '', music_info[4]).split(", ")  # Получение и сохранение остальных данных песни
            authors = info[0:-2]  # Получение и сохранение авторов песни
            len = info[-2]  # Получение и сохранение длинны песен
            link = info[-1]  # Получение и сохранение ссылки на песню

            if search_music != '':  # Условие если в фильтре что-то есть
                for tag in tags:  # Перебор всех тегов в песни
                    for author in authors:
                        if search_music in tag or search_music in author or search_music in name:
                            # Проверка на совпадение по тегу, автору или названию
                            return id, name, authors, len, link
                            # Возвращение данных найденных песен (id, название, автор(ы), длинна, ссылка)
            else:  # Блок иначе
                return id, name, authors, len, link
                # Возвращение данных найденных песен (id, название, автор(ы), длинна, ссылка)


def music_edit_part1(number_music):
    id_music = number_music - 1
    all_music = os.listdir("./musics/")  # Создание списка всех файлов музыки
    for music in all_music:  # Цикл перебора списка all_music
        with open(f"./musics/{music}", "r", encoding="utf8") as file:  # Открытие файла с названием music на чтение
            music_info = file.readlines()  # Создание массива данных песни
            id = music_info[1][:-1]  # Получение и сохранение id песни
            name = music_info[2][:-1]
            if id_music == id:
                tags = re.sub(r'[\n\[\]\']', '', music_info[3]).split(',')  # Получение и сохранение тегов песни
                result = ''
                for tag in tags:
                    if result == '':
                        result = tag
                    else:
                        result = f'{result}, {tag}'
            else:
                return False
    return name, result


def music_edit_part2(number_music, tags):
    id_music = number_music - 1
    tags_array = tags.split(", ")
    all_music = os.listdir("./musics/")  # Создание списка всех файлов музыки
    for music in all_music:  # Цикл перебора списка all_music
        with open(f"./musics/{music}", "r", encoding="utf8") as file:  # Открытие файла с названием music на чтение
            music_info = file.readlines()  # Создание массива данных песни
            id = music_info[1][:-1]  # Получение и сохранение id песни
            if id_music == id:
                music_info[1][:-1] = f"{tags_array}\n"
                return True


def delete_music_in_playlist(active_user, song_number):
    id = str(int(song_number) - 1)
    user_data = edit_u.get_file(active_user)  # Получение всех данных пользователя
    playlist_id = re.sub(r'[\[\]\' ]', '', user_data[14][:-1]).split(',')
    playlist_num = int(user_data[16][:-1])
    playlist_len = main.time_converter(user_data[17])
    all_music = os.listdir("./musics/")  # Создание списка всех файлов музыки
    for music in all_music:  # Цикл перебора списка all_music
        with open(f"./musics/{music}", "r", encoding="utf8") as file:  # Открытие файла с названием music на чтение
            music_info = file.readlines()  # Создание массива данных песни
            music_id = music_info[1][:-1]
            if id == music_id:
                music_last_info = re.sub(r'[\[\]\']', '', music_info[4]).split(',')  # Получение и сохранение информации о песне
                music_len = main.time_converter(music_last_info[-2])  # Конвертация времени из файла из Ч:М:С в секунды
                # Этап удаления музыки
                try:
                    playlist_id.remove(str(id))
                    playlist_len -= music_len
                    format_time = time.strftime("%H:%M:%S", time.gmtime(playlist_len))
                    playlist_num -= 1
                    playlist_tags = []
                    for music in all_music:
                        with open(f"./musics/{music}", "r", encoding="utf8") as file:  # Открытие файла с названием music на чтение
                            music_info = file.readlines()  # Создание массива данных песни
                            if music_info[1][:-1] in playlist_id:
                                music_tag = re.sub(r'[\n\[\]\']', '', music_info[3]).split(', ')
                                playlist_tags = list(filter(None, set(playlist_tags + music_tag)))
                                user_data[14] = f"{playlist_id}\n"
                                user_data[16] = f"{playlist_num}\n"
                                user_data[17] = f"{format_time}"
                                user_data[13] = f"{playlist_tags}\n"
                except:
                    print("Песни нет в плейлисте!")
            else:
                continue

    edit_user.set_file(active_user, user_data)

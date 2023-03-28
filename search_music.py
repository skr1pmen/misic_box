import os
import re


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
    return result


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

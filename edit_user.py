import re


def get_file(active_user):
    with open(f"./users/{active_user}.txt", "r", encoding="utf8") as user:  # Открытие файла активного пользователя для чтение
        return user.readlines()  # Возврат всех данных пользователя


def set_file(active_user, user_data):
    with open(f"./users/{active_user}.txt", "w", encoding="utf8") as user:  # Открытие файла активного пользователя для перезаписи
        i = 0  # Счётчик для цикла
        while i < len(user_data):  # Цикл перебора всех данных пользователя
            user.write(user_data[i])  # Построчная запись данных в файл
            i += 1  # Увеличиваем счётчик


def nationality(active_user):
    nationality = input("Кто вы по национальности? ")
    user_data = get_file(active_user)  # Получение всех данных пользователя

    user_data[5] = f"{nationality}\n"  # Перезапись данных о национальности пользователя

    set_file(active_user, user_data)  # Сохранение данных в файл пользователя
    return "Национальность добавлена!"  # Возвращаем успешный результат


def profession(active_user):
    profession = input("Укажите вашу профессию, если их много, то укажите их через запятую: ")
    profession = profession.split(", ")  # Форматируем полученных от пользователя данные, переводом в список
    user_data = get_file(active_user)  # Получение всех данных пользователя

    user_list = re.sub(r'[\n\[\]\' ]', '', user_data[6]).split(',')  # Удаляем из данных в файле лишние символы и переводим в список

    user_list.extend(profession)  # Метод exdend добавляет элементы массива в другой массив
    user_list = list(filter(None, set(user_list)))  # set() перевод массива в набор(в нём нет повторящихся элементов), после list() обратно переводит в список
    user_data[6] = f"{user_list}\n"  # Перезапись данных о професиях пользователя

    set_file(active_user, user_data)  # Сохранение данных в файл пользователя
    return "Профессии добавлены!"  # Возвращаем успешный результат


def hobby(active_user):
    hobby = input("Укажите ваше хобби, если их много, то укажите их через запятую: ")
    hobby = hobby.split(", ")  # Форматируем полученных от пользователя данные, переводом в список
    user_data = get_file(active_user)  # Получение всех данных пользователя

    user_list = re.sub(r'[\n\[\]\' ]', '', user_data[7]).split(',')  # Удаляем из данных в файле лишние символы и переводим в список

    user_list.extend(hobby)  # Метод exdend добавляет элементы массива в другой массив
    user_list = list(filter(None, set(user_list)))  # set() перевод массива в набор(в нём нет повторящихся элементов), после list() обратно переводит в список
    user_data[7] = f"{user_list}\n"  # Перезапись данных о хобби пользователя

    set_file(active_user, user_data)  # Сохранение данных в файл пользователя
    return "Хобби добавлены!"  # Возвращаем успешный результат

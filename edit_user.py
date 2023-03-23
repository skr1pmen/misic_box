import re


def get_file(active_user):
    with open(f"./users/{active_user}.txt", "r", encoding="utf8") as user:
        return user.readlines()


def set_file(active_user, user_data):
    with open(f"./users/{active_user}.txt", "w", encoding="utf8") as user:
        i = 0
        while i < len(user_data):
            user.write(user_data[i])
            i += 1


def nationality(active_user):
    nationality = input("Кто вы по национальности? ")
    user_data = get_file(active_user)

    user_data[5] = f"{nationality}\n"

    set_file(active_user, user_data)
    return "Национальность добавлена!"


def profession(active_user):
    profession = input("Укажите вашу профессию, если их много, то укажите их через запятую: ")
    profession = profession.split(", ")
    user_data = get_file(active_user)

    user_list = re.sub(r'[\n\[\]\' ]', '', user_data[6]).split(',')

    user_list.extend(profession)  # Метод exdend добавляет элементы массива в другой массив
    user_list = list(filter(None, set(user_list)))  # set() перевод массива в набор(в нём нет повторящихся элементов), после list() обратно переводит в список
    user_data[6] = f"{user_list}\n"

    set_file(active_user, user_data)
    return "Проффессии добавлены!"


def hobby(active_user):
    hobby = input("Укажите ваше хобби, если их много, то укажите их через запятую: ")
    hobby = hobby.split(", ")
    user_data = get_file(active_user)

    user_list = re.sub(r'[\n\[\]\' ]', '', user_data[7]).split(',')

    user_list.extend(hobby)  # Метод exdend добавляет элементы массива в другой массив
    user_list = list(filter(None, set(user_list)))  # set() перевод массива в набор(в нём нет повторящихся элементов), после list() обратно переводит в список
    user_data[7] = f"{user_list}\n"

    set_file(active_user, user_data)
    return "Проффессии добавлены!"
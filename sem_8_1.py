# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def enter_first_name():
    return input("Введите Имя абонента: ").title()


def enter_second_name():
    return input("Введите Фамилию абонента: ").title()


def enter_family_name():
    return input("Введите Отчество абонента: ").title()


def enter_phone_number():
    return input("Введите Номер телефона: ")


def enter_address_number():
    return input("Введите Адрес абонента: ").title()


def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name}, {surname}, {family}\n{number}\n{address}\n\n')


def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def search_line():
    print('выбирете для поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчетсво\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите номер варианта поиска: ')) - 1
    searched = input('Введите поисковые данные: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        # print([file.read()])
        # file.seek(0)
        # print(file.readlines())
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item, end='\n\n')


def interface():
    cmd = 0
    while cmd != '4':
        print("Выберите действие: \n"
              "1. Добавить контакт\n"
              "2. Вывести все контакты\n"
              "3. Поиск контакта\n"
              "4. Выход\n")
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4'):
            print("Не корректный ввод")
            cmd = input("Введите действие: ")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                print("Всего доброго!")


def del_info():
    print("Выберите информацию для удаления:\n"
          "1. Имя\n"
          "2. Фамилия\n"
          "3. Очество\n"
          "4. Телефон\n"
          "5. Адрес\n"
          "6. Удалить контакт")
    index = int(input("Введите вариант: ")) - 1
    searched = input("Введите данные поиска: ").title()

    with open("book.txt", "r", encoding="utf-8") as file:
        data = file.read().strip().split("\n\n")

    new_data = []
    for item in data:
        if searched in item:
            if index < 5:
                # continue
                contact_info = item.replace("\n", " ").split()
                if len(contact_info) >= index + 1 and searched == contact_info[index]:
                    # field_to_delete = contact_info[index]
                    # if searched == field_to_delete:
                    contact_info[index] = "удалено"
                    new_data.append(f"{contact_info[0]} {contact_info[1]} {contact_info[3]}\n{contact_info[4]}\n")
                else:
                    new_data.append(item)
            else:
                new_data.append(item)

    with open("book.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(new_data))   

def chenge():
    print("Выберите вариант, для применения изменения: \n"
          "1. Имя\n"
          "2. Фамилия\n"
          "3. Отчество\n"
          "4. Телефон\n"
          "5. Адрес")
    
    index = int(input("Введите вариант действия: ")) - 1
    searched = input("Введите данные для изменения: ").title()
    replacement = input("Введите новые данные: ").title()

    with open("book.txt", "r", encoding="utf-8") as file:
        data = file.read().strip().split("\n\n")

    new_data = []
    check = False

    for item in data:
        contact_info = item.replace("\n", " ").split()
        if len(contact_info) >= index + 1:
            if contact_info[index] == searched:
                check = True
                contact_info[index] = replacement
                new_data.append(f"{contact_info[0]} {contact_info[1]} {contact_info[2]} {contact_info[3]} {contact_info[4]}\n")
            else:
                new_data.append(item)
        else:
            new_data.append(item)

    if not check:
        print("Нет совпадений. Введите новые данные")

    with open("book.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(new_data))


interface()

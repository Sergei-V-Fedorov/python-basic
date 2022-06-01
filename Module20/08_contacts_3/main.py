# проверка на корректный номер действия
def is_correct_request(user_request):
    return user_request in ('1', '2', '3')


# добавление контакта
def add_contact(user_book):
    new_contact = input("Введите имя и фамилию нового контакта (через пробел): ")
    new_contact = tuple(new_contact.split())
    if new_contact in user_book:
        print("Такой человек уже есть в контактах.")
    else:
        phone_number = int(input("Введите номер телефона: "))
        user_book[new_contact] = phone_number
    print("Текущий словарь контактов:", user_book, '\n')


# поиск контакта
def search_contact(user_book):
    surname = input("Введите фамилию для поиска: ").lower()
    for contact in user_book:
        if surname == contact[1].lower():
            print(*contact, user_book[contact], '\n')
            break
    else:
        print("Контакт не найден\n")


telephone_book = {}
while True:
    request = input("Введите номер действия:\n  "
                    "1. Добавить контакт\n  "
                    "2. Найти человека\n  "
                    "3. Выйти из меню\n")

    if is_correct_request(request):
        request = int(request)

        if request == 3:  # выход
            break

        elif request == 2:  # поиск контакта
            search_contact(telephone_book)

        elif request == 1:  # добавление контакта
            add_contact(telephone_book)

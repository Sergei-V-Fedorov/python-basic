import os.path


# пишем костыли, чтобы диск получить
def get_drive():
    drive = os.getcwd()
    drive, tail = os.path.splitdrive(drive)
    if not drive:
        drive = "/home"
    return drive


# запись в файл
def write_text_file(target, user_text):
    with open(target, 'w') as text_file:
        text_file.write(user_text)


# вывод на печать содержимого файла
def print_text_file(target):
    user_text = None
    short_name = os.path.split(target)
    with open(target, 'r') as text_file:
        user_text = text_file.read()

    print(f"Содержимое файла '{short_name[1]}':")
    print(user_text)


text = input("Введите строку: ")

root = get_drive()  # корень

print("\nКуда хотите сохранить документ?", "Введите последовательность папок (через пробел): ")
path_to_text = input().split()
path_to_text = os.path.join(root, *path_to_text)

if os.path.exists(path_to_text):
    file_name = input("\nВведите имя файла: ")
    if file_name.endswith(".txt"):  # расширение уже введено?
        file_name = file_name[:-4]
    full_file_name = os.path.join(path_to_text, file_name+".txt")
    if os.path.exists(full_file_name):  # есть файл
        answer = input("Вы действительно хотите перезаписать файл? (да/нет) ")
        if answer == "да":
            write_text_file(full_file_name, text)
            print("Файл успешно перезаписан!")
        print_text_file(full_file_name)
    else:
        write_text_file(full_file_name, text)
        print("Файл успешно сохранён!")
        print_text_file(full_file_name)
else:
    print(f"Указан несуществующий путь {path_to_text}")

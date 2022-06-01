import os


# вычисляет длину строки, если она больше 3, не считая '\n'
def calculate_length(user_string):
    try:
        if user_string.endswith('\n'):
            user_string = user_string[:-1]
        if len(user_string) < 3:
            raise TypeError
        return len(user_string)
    except TypeError:
        return None


# вывод на печать содержимого файла
def print_text_file(target):
    short_name = os.path.split(target)
    with open(target, 'r') as text_file:
        user_text = text_file.read()
    print(f"Содержимое файла '{short_name[1]}':")
    print(user_text)


file_name = "people.txt"
print_text_file(file_name)
print("\nОтвет в консоли:")

row = 0
symbols_count = 0

with open(file_name, 'r') as ifile:
    for line in ifile.readlines():
        length = calculate_length(line)
        if length:
            symbols_count += length
        else:
            print(f"Ошибка: менее трёх символов в строке {row}.")
        row += 1
print("Общее количество символов:", symbols_count)

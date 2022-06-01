import os
from collections.abc import Generator


def count_strings(user_list: list) -> Generator:
    for name in user_list:
        with open(name, 'r') as py_file:
            multistring_comment = False
            str_count = 0

            for line in py_file:
                line = line.strip()
                if line and not line.startswith('#'):  # не пустые строки и не однострочные комментарии
                    # многострочные комментарии
                    if line.startswith('"""') or line.startswith("'''"):  # начало комментария
                        multistring_comment = True
                        continue
                    if multistring_comment:
                        if line.endswith('"""') or line.endswith("'''"):  # конец комментария
                            multistring_comment = False
                        continue

                    str_count += 1
        yield str_count


search_dir = input("Введите имя директории: ")
if not os.path.exists(search_dir):
    raise FileNotFoundError("Такой директории не существует")

# получаем список питоновских файлов
file_list = os.listdir(search_dir)
file_list = [os.path.join(search_dir, file_name)
             for file_name in file_list
             if file_name.endswith(".py")]
if file_list:
    file_list.sort()

    generator = count_strings(file_list)
    total = 0
    for filename, code_quantity in zip(file_list, generator):
        total += code_quantity
        print(f"В файле {filename} ==> {code_quantity} строк кода")

    print("\nCуммарное кол-во строк кода во всех файлах", total)
else:
    print("В данной директории нет файлов *.py")

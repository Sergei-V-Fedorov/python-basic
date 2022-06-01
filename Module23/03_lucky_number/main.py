import random
import os


# вывод на печать содержимого файла
def print_text_file(target):
    short_name = os.path.split(target)
    with open(target, 'r') as text_file:
        user_text = text_file.read()
    print(f"\nСодержимое файла '{short_name[1]}':")
    print(user_text)


total = 0
file_name = "out_file.txt"
probability = [True if index == 0 else False
               for index in range(13)]

try:
    with open(file_name, 'w') as ofile:

        while total < 777:
            number = int(input("Введите число: "))
            chance = random.choice(probability)  # 1/13
            if chance:  # генерация случайного исключения
                new_exc = random.choice(Exception.__subclasses__())
                raise new_exc

            ofile.write(str(number) + '\n')
            total += number

        print("Вы успешно выполнили условие для выхода из порочного цикла!")
except new_exc:
    print("Вас постигла неудача!\nСлучайное исключение", new_exc.__name__)
finally:
    print_text_file(file_name)

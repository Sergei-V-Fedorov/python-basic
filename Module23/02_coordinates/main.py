import random
import math


def f(x, y):
    try:
        x += random.randint(0, 5)
        y += random.randint(0, 10)
        return x / y
    except ZeroDivisionError:
        # вставляем nan, чтобы сохранить длину ряда, но это создает некоторые трудности при сортировке
        return math.nan


def f2(x, y):
    try:
        x -= random.randint(0, 5)
        y -= random.randint(0, 10)
        return y / x
    except ZeroDivisionError:
        # вставляем nan, чтобы сохранить длину ряда, но это создает некоторые трудности при сортировке
        return math.nan


# возвращает список координат
def read_coordinates(user_file):
    result = []
    try:
        with open(user_file, 'r') as tf:
            result = [row.split() for row in tf]
            result = [tuple(map(int,
                                pair))
                      for pair in result]
    except FileNotFoundError:
        print(f"Ошибка: файл {user_file} не найден")
    except TypeError:
        print(f"Ошибка: файл {user_file} содержит некорректные данные")
    finally:
        return result


# вывод результатов
def write_results(user_file_name, results_1, results_2):
    rand_number = random.randint(0, 100)
    with open(user_file_name, 'w') as tf:
        for pair in zip(results_1, results_2):
            result = sorted([rand_number, *pair])
            result = [str(item) for item in result]
            tf.write(" ".join(result) + '\n')


file_name = "coordinates.txt"
output_name = "result.txt"
try:
    coordinates = read_coordinates(file_name)
    if coordinates:

        f_results = [f(coord_x, coord_y)  # значения первой функции
                     for coord_x, coord_y in coordinates]

        f2_results = [f2(coord_x, coord_y)  # значения второй функции
                      for coord_x, coord_y in coordinates]

        write_results(output_name, f_results, f2_results)  # запись результатов
except Exception:
    print("Что-то пошло не так")

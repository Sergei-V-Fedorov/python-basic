# выводит плоский список
def flatten_list(user_list):
    result = []
    while user_list:  # пока список не пустой
        first_element = user_list.pop(0)  # Удаляем первый элемент
        if isinstance(first_element, tuple):  # если он кортеж
            first_element = list(first_element)  # то преобразуем в список
        if isinstance(first_element, list):  # если список
            # то записываем его в конец исходного списка, уменьшая вложенность на 1
            user_list.extend(first_element)
        else:  # считаем, что число
            result.append(first_element)  # добавляем в результат
    return result  # плоский список


def my_sum(*args):
    result = 0
    for argument in args:
        if isinstance(argument, (int, float)):  # число суммируем
            result += argument
        elif isinstance(argument, tuple):  # кортеж сглаживаем и прибавляем его сумму
            # кортеж неизменяемый, преобразуем его в список
            flat_tuple = flatten_list(list(argument))
            result += sum(flat_tuple)
        elif isinstance(argument, list):  # список сглаживаем и прибавляем его сумму
            flat_list = flatten_list(argument)
            result += sum(flat_list)
    print("Ответ в консоли:", result)


# tests
'''test_1 = [[1, 2, [3]], [1], 3]  # 10
test_2 = 1, 2, 3, 4, 5  # 15
test_3 = [[1, [2], ([3], 5)], [[6]], (4, 7, (8,))]  # 36

my_sum(test_1)  # тест - вложенный нерегулярный список списков. Сумма = 10

my_sum(1, 2, 3, 4, 5)  # тест - последовательность простых чисел. Сумма = 15

my_sum(test_2)  # тест - кортеж одномерный. Сумма = 15

my_sum(test_3)  # тест - адская хрень. Сумма = 36

my_sum(test_2, test_2, test_2)  # тест - параметры. Сумма = 45

my_sum(list(test_2), test_2)  # тест - параметры. Сумма = 30

my_sum([[1, 2, 3], [10, 20], 1], test_2)  # тест - параметры. Сумма = 52

# почему не работает? при объединении в кортеж test_1, test_2, test_3 списки оказываются пустыми
my_sum(test_1, test_2, test_3)  # тест - параметры. Сумма = 61'''

def my_zip_2(iterable_1, iterable_2):
    length = min(len(iterable_1), len(iterable_2))
    iterator_1 = iter(iterable_1)
    iterator_2 = iter(iterable_2)
    result = [(next(iterator_1), next(iterator_2)) for _ in range(length)]
    return result


# тест 1
'''first_iterable = "abcdef"
second_iterable = (10, 20, 30, 40)'''

# тест 2
'''first_iterable = range(10, 101, 10)
second_iterable = ['a', 'b', 'c', 'd']'''

# тест 3
'''first_iterable = {"name": "Sergei", "surname": "Fedorov"}
second_iterable = ['a', 'b', 'c', 'd']'''

# тест 4
first_iterable = set([13, 18, 43, 56, 73, 95])
second_iterable = ['a', 'b', 'c', 'd']

print("Итерируемая переменная:", first_iterable)
print("Итерируемая переменная:", second_iterable)

my_zip_result = my_zip_2(first_iterable, second_iterable)

print(my_zip_result)

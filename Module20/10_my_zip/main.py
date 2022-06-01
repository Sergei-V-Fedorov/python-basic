def my_zip(iterable_1, iterable_2):
    # словари нужно преобразовывать к списку ключей
    allowed_type = (str, list, tuple, range)
    if isinstance(iterable_1, allowed_type) and isinstance(iterable_2, allowed_type):
        length = min(len(iterable_1), len(iterable_2))

        generator = ((iterable_1[index], iterable_2[index]) for index in range(length))
        return generator

# тест 1
first_iterable = "abcd"
second_iterable = (10, 20, 30, 40)

# тест 2
'''first_iterable = range(10, 101, 10)
second_iterable = ['a', 'b', 'c', 'd']'''

print("Итерируемая переменная:", first_iterable)
print("Итерируемая переменная:", second_iterable)

new_generator = my_zip(first_iterable, second_iterable)

print(new_generator)
for items in new_generator:
    print(items)

# я не знаю, как решить, не меняя код
# генератор может заменить циклы. как выйти из цикла с помощью генератора не знаю
# break идеально для дострочного выхода
from collections.abc import Generator


def pair_multiplier(sequence_1: list, sequence_2: list, need_find: int) -> Generator:
    for num_1 in sequence_1:
        for num_2 in sequence_2:
            mult = num_1 * num_2
            yield f"{num_1} {num_2} {mult}"
            if mult == need_find:
                yield "Found!!!"
                return

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

'''can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break'''

generator_1 = pair_multiplier(list_1, list_2, to_find)
for multiplier in generator_1:
    print(multiplier)

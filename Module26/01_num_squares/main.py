from collections.abc import Iterable, Generator


class SquareIntegers:

    def __init__(self, num: int) -> None:
        self.limit = num
        self.__counter = 0

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> int:
        self.__counter += 1
        if self.__counter > self.limit:
            raise StopIteration
        else:
            return self.__counter ** 2


def generator_2(user_number: int) -> Generator:
    for i in range(1, user_number + 1):
        yield i ** 2


number = int(input("Введите число: "))

generator_1 = (num ** 2 for num in range(1, number + 1))
print(f"Последовательность квадратов от 1 до {number}:", end=' ')
for num in generator_1:
    print(num, end=' ')

print(f"\nПоследовательность квадратов от 1 до {number}:", end=' ')
for num in generator_2(number):
    print(num, end=' ')

generator_3 = SquareIntegers(number)
print(f"\nПоследовательность квадратов от 1 до {number}:", end=' ')
for num in generator_3:
    print(num, end=' ')

from collections.abc import Iterable


class Hofstadter:

    def __init__(self, sequence: list) -> None:
        self.__sequence = self.set_sequence(sequence)
        self.__count = 0

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> int:
        self.__count += 1
        if self.__count > 2:
            n = self.__count - 1
            member = self.__sequence[n - self.__sequence[n - 1]] + \
                     self.__sequence[n - self.__sequence[n - 2]]
            self.__sequence.append(member)
            return member
        else:
            return 1

    def set_sequence(self, sequence: list) -> list:
        if sequence == [1, 1]:
            return sequence
        else:
            raise ValueError("Введены неправильные члены последовательности")


generator = Hofstadter([1, 1])

print('n'.center(2),  'Q(n)'.center(7))
for index, item in enumerate(generator, start=1):
    print(str(index).ljust(5), str(item).ljust(5))
    if index > 19:
        break

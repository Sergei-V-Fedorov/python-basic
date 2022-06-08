import os
import typing


class File:
    """ Конекст-меренджер """

    def __init__(self, file_name: str, mode='r') -> None:
        self.file_name = file_name
        self.mode = mode

    def if_not_exists(self) -> None:
        """ Меняем опцию, если файл не существует """
        if not os.path.exists(self.file_name):
            self.mode = 'w'

    def __enter__(self) -> typing.TextIO:
        """ возвращает дескриптор файла """
        self.if_not_exists()
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True

# в меняем режим для несуществующего файла
with File('result.txt', 'r') as file:
    file.write('read of non-existed file' + '\n')

# игнорирование ошибки - использование write при чтении
with File('result.txt', 'r') as file:
    file.write('read of non-existed file' + '\n')

# читаем файл
with File('result.txt', 'r') as file:
    file.read()

# запись
with File('result.txt', 'w') as file:
    file.write('write to existing file' + '\n')

# append
with File('result.txt', 'a') as file:
    file.write('add to existing file' + '\n')

with File('result.txt', 'r') as file:
    line = file.read()
print("вот что мы записали в файл:\n" + line)


import os
from collections.abc import Generator


def gen_files_path(start_dir: str, stop_dir: str) -> Generator:
    for dirpath, dirnames, filenames in os.walk(start_dir):
        for filename in filenames:
            yield os.path.join(dirpath, filename)
        if os.path.basename(dirpath) == stop_dir:
            return


from_dir = "/home"

answer = input("Ввести корневую директорию (по-умолчанию /home) (y/n): ")
if answer == 'y':
    from_dir = input("Введите корневую директорию (например: /home): ")
to_dir = input("Введите директорию, которую нужно найти (например: Downloads) ")

if not os.path.exists(from_dir):
    raise FileNotFoundError("Не существует такой директории")

generator = gen_files_path(start_dir=from_dir, stop_dir=to_dir)

for file_name in generator:
    print(file_name)

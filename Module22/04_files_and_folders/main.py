import os


# считает размер директории, кол-во вложенных директорий и файлов
def count_dir_size(user_path):
    dir_size = 0
    dir_count = 0
    file_count = 0
    if os.path.isdir(user_path):
        dir_content = os.listdir(user_path)
        for item in sorted(dir_content):
            item = os.path.join(user_path, item)
            if os.path.isfile(item):
                dir_size += os.path.getsize(item)
                file_count += 1
            else:
                dir_size += count_dir_size(item)[0]
                file_count += count_dir_size(item)[2]
                dir_count += 1
    else:
        print(f"Директории {user_path} не существует")
        return None
    return dir_size, dir_count, file_count


# test
'''module22_dir = os.path.abspath(os.path.join(".."))'''

module22_dir = input("Введите путь до каталога: ")
result = count_dir_size(module22_dir)
if result:
    total_size, total_dir, total_files = result
    print(f"Размер каталога (в Кб): {total_size/1024:,f}")
    print("Количество подкаталогов:", total_dir)
    print("Количество файлов:", total_files)


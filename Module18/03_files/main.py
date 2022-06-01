illegal_symbols = tuple("@№$%^&\*()")
extensions = (".txt", ".docx")

file_name = input("Название файла: ")

if file_name.startswith(illegal_symbols):
    print("\nОшибка: название начинается на один из специальных символов.")
elif not file_name.endswith(extensions):
    print("\nОшибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("\nФайл назван верно.")

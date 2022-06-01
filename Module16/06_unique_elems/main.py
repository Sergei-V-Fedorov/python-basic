# Заполнение списка числами args = int, str
def fill_list(length, order):  # возвращает заполненный список
    result = []
    for index in range(length):
        number = int(input(f"Введите {index + 1}-е число для {order} списка: "))
        result.append(number)
    return result


first_list = fill_list(3, "первого")
second_list = fill_list(7, "второго")

print("\nПервый список:", first_list)
print("Второй список:", second_list)

first_list.extend(second_list)

# Словарь с ключи = цифры из first_list, подсчитаем кол-во цифр и удалим повторяющиеся
temporary = dict.fromkeys(first_list)
for key in temporary:
    count = first_list.count(key)
    for time in range(count - 1):  # удаляем count-1 цифр
        first_list.remove(key)

print("Новый первый список с уникальными элементами:", first_list)

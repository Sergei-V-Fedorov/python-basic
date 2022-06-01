# проверка корректности вводимых цифр
def is_correct(left, right, total):
    result = (1 <= left <= right) and (left <= right <= total)
    return result


number_skittles = int(input("Количество палок: "))
number_shots = int(input("Количество бросков: "))

skittles = ['I'] * number_skittles

for shot in range(number_shots):
    while True:
        hits = input("Введите через пробел диапазон сбитых кеглей: ")
        hits = list(map(int, hits.split()))
        if is_correct(hits[0], hits[1], number_skittles):
            print(f"Бросок {shot + 1}. Сбиты палки с номера {hits[0]}\nпо номер {hits[1]}.")
            skittles[hits[0]-1 : hits[1]] = ['.']*(hits[1] - hits[0] + 1)
            break
        else:
            print("Неверный ввод. 1 ≤ Left ≤ Right ≤ N")

skittles = ''.join(skittles)
print("\nРезультат:", skittles)

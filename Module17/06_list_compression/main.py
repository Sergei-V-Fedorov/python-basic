# Переставляет нули в конец в original, возвращает сжатый массив
def compress_array(original):
    result = [number for number in sequence if number]
    tail = [0]*(len(original) - len(result))
    original[:] = result[:]
    original.extend(tail)
    return result


length = int(input("Количество чисел в списке: "))
sequence = input("Список до сжатия: ")
sequence = list(map(int, sequence[1:-1].split(', ')))

compressed = compress_array(sequence)

print("Список после сжатия:", compressed)

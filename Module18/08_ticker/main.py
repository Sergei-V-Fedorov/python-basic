# возвращает строку со сдвигом вправо
def shift_string(original_string, shift_right):
    string_length = len(original_string)
    slice_index = shift_right % string_length
    result = original_string[slice_index:] + original_string[:slice_index]
    return result


# возвращает список всех комбинаций строк со сдвигом 1 символ вправо
def find_combinations(original_string):
    result = []
    for index in range(len(original_string)):
        permutation = shift_string(original_string, index)
        result.append(permutation)
    return result


first_line = input("Первая строка: ")
second_line = input("Первая Вторая: ")

permutations = find_combinations(first_line)
if second_line in permutations:
    shift = permutations.index(second_line)
    print(f"\nПервая строка получается из второй со сдвигом {shift}.")
else:
    print("\nПервую строку нельзя получить из второй с помощью циклического сдвига.")

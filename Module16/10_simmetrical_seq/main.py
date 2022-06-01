# возвращает список чисел, которые нужно приписать справа
def symmetry(original_list):
    palindrome = original_list.copy()
    result = []
    while palindrome != palindrome[::-1]:
        first = palindrome.pop(0)
        result.append(first)
    return result


quantity = int(input("Кол-во чисел: "))
sequence = []
for index in range(1, quantity + 1):
    number = int(input("Число: "))
    sequence.append(number)

print("\nПоследовательность:", sequence)
absent_numbers = symmetry(sequence)
absent_numbers.reverse()
print("Нужно приписать чисел:", len(absent_numbers))
print("Сами числа:", absent_numbers)

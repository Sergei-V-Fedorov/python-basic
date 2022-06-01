
def digit_sum(number):  # сумма цифр числа
    result = 0
    while number:
        result += number % 10
        number //= 10
    return result

def digit_count(number):  # кол-во цифр
    result = 0
    while number:
        result += 1
        number //= 10
    return result

def sum_in_range(number):  # сумма чисел от 1 до number
    return sum(range(1, number + 1))

number = int(input("Введите число: "))

print("Условие задачи и примера работы программы не соответствуют. ")
choice = int(input("0 - вычислить сумму от 1 до N; 1 - сумму всех цифр числа N? "))

if choice == 0:
    summa = sum_in_range(number)
else:
    summa = digit_sum(number)

count = digit_count(number)
print("\nСумма чисел:", summa)
print("Количество цифр в числе:", count)
print("Разность суммы и количества цифр:", summa - count)
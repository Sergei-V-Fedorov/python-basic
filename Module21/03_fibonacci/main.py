# цикл
def fibonacci_1(number):
    if number == 1:
        return 1

    previous, current = 0, 1
    for item in range(1, number):
        previous, current = current, current + previous
    return current


# рекурсивно
def fibonacci_recursion(number):
    if 1 <= number <= 2:
        return 1

    return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)


request = int(input("Введите позицию числа в ряде Фибоначчи: "))
if request > 0:
    fibonacci_number = fibonacci_1(request)
    print("Число:", fibonacci_number)
    print("Рекурсия")
    print("Число:", fibonacci_recursion(request))

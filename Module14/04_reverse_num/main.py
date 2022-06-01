import math

n = float(input("Введите первое число: "))
m = float(input("Введите второе число: "))


def float_reverse(number):  # через math.modf() и строки
    result = ""
    if number < 0:  # отрицательное число
        result = "-"
        number *= -1
    frac_number, int_number = math.modf(number)
    # ограничимся точностью 10e-2, как в примере
    result += str(int(int_number))[::-1] + "." + str(int(frac_number * 100))[::-1]
    return result

n = float_reverse(n)
m = float_reverse(m)
print("Первое число наоборот:", n)
print("Второе число наоборот:", m)
print("Сумма:", float(n) + float(m))



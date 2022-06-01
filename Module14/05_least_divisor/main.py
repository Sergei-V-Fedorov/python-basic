def lesser_divider(number):
    result = 2
    while number % result:
        result += 1
    return result

n = int(input("Введите число: "))
while n < 1:
    n = int(input("Число должно быть больше 1: "))

print("Наименьший делитель, отличный от единицы:", lesser_divider(n))

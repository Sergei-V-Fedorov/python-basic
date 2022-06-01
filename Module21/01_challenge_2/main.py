# выводит числа от 1 до N
def range_of_natural(right_limit):
    if right_limit == 1:
        print(right_limit)
    else:
        range_of_natural(right_limit-1)
        print(right_limit)


number = int(input("Введите num: "))
if number > 0:
    range_of_natural(number)

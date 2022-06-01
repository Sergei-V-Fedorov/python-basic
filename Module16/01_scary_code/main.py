a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

# first_number = 5

a.extend(b)
count = a.count(5)
print("Кол-во цифр 5 при первом объединении:", count)

while 5 in a:
    a.remove(5)

a.extend(c)
count = a.count(3)
print("Кол-во цифр 3 при втором объединении:", count)
print("Итоговый список:", a)

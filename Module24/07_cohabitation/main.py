import CircleOfLife as cl
import random

house = cl.House()
artem = cl.Human("Артём")
girl_friend = cl.Human("Елена")
artem.house = house
girl_friend.house = house
dwellers = [artem, girl_friend]

print("Начальное состояние")
for dweller in dwellers:
    dweller.print_status()

day = 1
while True:
    print(f"\nДень {day}")
    '''dwellers[0].print_status()
    dwellers[1].print_status()'''

    cube = random.randint(1, 6)
    for dweller in dwellers:
        if dweller.alive < 20 or cube == 2:
            print(dweller.name, "пошел есть")
            dweller.eat()
        elif dweller.house.fridge < 10:
            print(dweller.name, "пошел в магазин")
            dweller.shopping()
        elif dweller.house.table < 50 or cube == 1:
            print(dweller.name, "пошел работать")
            dweller.work()
        else:
            print(dweller.name, "пошел играть")
            dweller.play()

    if dwellers[0].alive < 0:
        print(f"{dwellers[0].name} не хватило сил жить в этом суровом мире!\nИгра закончена")
        break
    if dwellers[1].alive < 0:
        print(f"{dwellers[1].name} не хватило сил жить в этом суровом мире!\nИгра закончена")
        break

    day += 1
    if day == 366:
        print(f"\nПрошел год. Ребята выжили и скопили {house.table}")
        break

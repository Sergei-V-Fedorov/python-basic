import Family
import random

husband = Family.Husband("Артём")
wife = Family.Wife("Марина")
cat = Family.Cat("Master of the Universe")
house = Family.House()
wife.house = house
husband.house = house
cat.house = house

cat_actions = {1: cat.eat, 2: cat.sleep, 3: cat.sharp_claws}
husband_actions = {1: husband.eat, 2: husband.play, 3: husband.work, 4: husband.pet}
wife_actions = {1: wife.eat, 2: wife.shopping, 3: wife.pet, 4: wife.clean, 5: wife.buy_coat,}

day = 1

while True:
    print(f"\nДень {day}")
    house.add_dirt()  # добавляем грязь
    print(house)
    husband.piggery()  # уменьшаем счастье, если грязно
    wife.piggery()


    print("==>", cat)  # действия кота
    if cat.satiety <= 10:
        cat_actions[1]()
    else:
        action = random.randint(1, 3)
        cat_actions[action]()

    print("==>", husband)  # действия мужа
    if husband.satiety <= 10:
        husband.eat(amount=10)
    elif house.table < 100:
        husband.work()
    elif husband.happy < 10:
        action = random.randint(3, 4)
        husband_actions[action]()
    else:
        action = random.randint(1, 4)
        husband_actions[action]()

    print("==>", wife)  # действия жены
    if wife.satiety <= 10:
        wife.eat(amount=10)
    elif house.table > 300 and (house.fridge <= 50 or house.cat_food <= 30):
        wife.shopping(food=100, wiskas=50)
    elif house.dirt > 90:
        wife.clean()
    elif house.fridge < 60:
        wife.shopping(food=30, wiskas=0)
    elif house.cat_food < 20:
        wife.shopping(food=0, wiskas=30)
    elif house.table >= 350 * 2:
        wife.buy_coat()
    elif wife.happy < 10:
            wife.pet()
    else:
        action = random.randint(1, 4)
        wife_actions[action]()

    day += 1
    if cat.satiety < 0:
        print(cat.name + "Умер от голода")
        break
    if husband.satiety < 0 or wife.satiety < 0:
        print(cat.name + "стал сиротой, не кому о нем позаботиться")
        break
    if day == 366:
        lost_money = husband.income - house.table + 100
        eaten_food = wife.total_food - house.fridge + 50
        eaten_wiskas = wife.total_wiskas - house.cat_food + 30
        print("\nПрошел год. Заработано {0}, потрачено {1}.\n"
              "Куплено шуб {2}. Съедено {3} и кошачьего корма {4}".format(
            husband.income, lost_money, wife.coats, eaten_food, eaten_wiskas))
        break

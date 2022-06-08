class Dwellers:
    def __init__(self, name, satiety=30):
        self.name = name
        self.satiety = satiety
        self.house = House()

    def eat(self, amount=30):
        print(f"{self.name} покушал")
        if self.house.fridge < 0:
            raise BaseException("Еды совсем не осталось")
        self.satiety += amount
        self.house.fridge -= amount


class Slaves(Dwellers):

    def __init__(self, name, satiety=30, happy=100):
        super().__init__(name, satiety)
        self.happy = happy

    def pet(self):
        print(f"{self.name} погладил кота")
        self.happy += 5
        self.satiety -= 10

    def piggery(self, amount=10):
        if self.house.dirt > 90:
            print(f"{self.name} не любит жить в грязи")
            self.happy -= amount

    def __str__(self):
        return "{0}, сытость {1}, счастье {2}".format(
            self.name, self.satiety, self.happy)


class Cat(Dwellers):

    def sleep(self):
        print(f"{self.name} уснул")
        self.satiety -= 10

    def sharp_claws(self):
        print(f"{self.name} поточил когти")
        self.satiety -= 10
        self.house.dirt += 5

    def eat(self, amount=10):
        print(f"{self.name} покушал немножко")
        if self.house.cat_food < 0:
            raise BaseException("Кошачьего корма совсем не осталось")
        self.satiety += 2 * amount
        self.house.cat_food -= amount

    def __str__(self):
        return "{0}, сытость {1}".format(
            self.name, self.satiety)


class Wife(Slaves):
    total_food = 0
    total_wiskas = 0
    coats = 0

    def shopping(self, food=30, wiskas=20):
        print(f"{self.name} сходила в магазин")
        '''if self.house.table < 0:
            raise BaseException("Совсем нет денег")'''
        money = food + wiskas
        if money > self.house.table:
            raise BaseException("Мало денег для покупки еды")
        self.satiety -= 10
        self.house.fridge += food
        self.house.cat_food += wiskas
        self.house.table -= money
        self.total_food += food
        self.total_wiskas += wiskas

    def buy_coat(self):
        print(f"{self.name} купила шубку")
        self.satiety -= 10
        self.house.table -= 350
        self.happy += 60
        self.coats += 1

    def clean(self, amount=100):
        print(f"{self.name} убрала в доме")
        self.satiety -= 10
        if self.house.dirt >= amount:
            self.house.dirt -= amount
        else:
            self.house.dirt = 0


class Husband(Slaves):
    income = 0

    def work(self, amount=10):
        print(f"{self.name} пошел на работу")
        self.satiety -= amount
        self.house.table += 150
        self.income += 150

    def play(self, amount=20):
        print(f"{self.name} поиграл в PlayStation")
        self.satiety -= 10
        self.happy += amount


class House:

    def __init__(self, food=50, money=100, cat_food=30, dirt=0):
        self.fridge = food
        self.table = money
        self.cat_food = cat_food
        self.dirt = dirt

    def add_dirt(self, amount=5):
        self.dirt += amount

    def __str__(self):

        return "Дома: {0} еды, {1} кошачьего корма, {2} денег, {3} грязи".format(
            self.fridge, self.cat_food, self.table, self.dirt)

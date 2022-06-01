class Human:

    def __init__(self, name, alive=50):
        self.name = name
        self.alive = alive
        self.house = House()

    def eat(self, count=10):
        self.alive += count
        self.house.fridge -= count // 2
        self.print_status()

    def print_status(self):
        print(f"{self.name}: сытость {self.alive}, "
              f"денег {self.house.table}, "
              f"еды {self.house.fridge}")

    def work(self, count=10):
        self.house.table += count * 5
        self.alive -= 2 * count
        self.print_status()

    def play(self, count=5):
        self.alive -= count
        self.print_status()

    def shopping(self, count=10):
        self.house.fridge += count * 50
        self.house.table -= count * 2
        self.print_status()


class House:

    def __init__(self, food=50, money=0):
        self.fridge = food
        self.table = money

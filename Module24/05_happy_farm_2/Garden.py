class Potato:
    states = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print("Картошка {0} сейчас {1}".format(
            self.index, self.states[self.state])
        )

    def is_ripe(self):
        return True \
            if self.state == 3 \
            else False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print("Картошка прорастает")
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print("Картошка еще не созрела\n")
            return False
        else:
            print("Вся картошка созрела. Можно собирать\n")
            return True


class Gardener:

    def __init__(self, name):
        self.name = name
        self.gardens = []

    def add_garden(self, *args):
        for arg in args:
            self.gardens.append(arg)

    def take_care(self, garden_index):
        if 0 <= garden_index < len(self.gardens):
            if not self.gardens[garden_index].are_all_ripe():
                self.gardens[garden_index].grow_all()

    def take_harvest(self, garden_index):
        if 0 <= garden_index < len(self.gardens):
            if self.gardens[garden_index].are_all_ripe():
                for potato in self.gardens[garden_index].potatoes:
                    potato.state = 0
                    potato.print_state()
                print("Весь урожай собран\n")
            else:
                print("Картошка еще не созрела. Рано убирать\n")

class Element:  # тестовый класс
    name = None


class Lightning:
    name = "Молния"


class Magma:
    name = "Лава"


class Storm:
    name = "Шторм"


class Steam:
    name = "Пар"


class Dirt:
    name = "Грязь"


class Dust:
    name = "Пыль"


class Water:
    name = "Вода"

    def __add__(self, other):
        if type(other) == Air:
            return Storm()
        elif type(other) == Fire:
            return Steam()
        elif type(other) == Terra:
            return Dirt()
        else:
            return Element()


class Fire:
    name = "Огонь"

    def __add__(self, other):
        if type(other) == Water:
            return Steam()
        elif type(other) == Air:
            return Lightning()
        elif type(other) == Terra:
            return Magma()
        else:
            return Element()


class Terra:
    name = "Земля"

    def __add__(self, other):
        if type(other) == Water:
            return Dirt()
        elif type(other) == Air:
            return Dust()
        elif type(other) == Fire:
            return Magma()
        else:
            return Element()


class Air:
    name = "Воздух"

    def __add__(self, other):
        if type(other) == Water:
            return Storm()
        elif type(other) == Terra:
            return Dust()
        elif type(other) == Fire:
            return Lightning()
        else:
            return Element()


class SuperElement:  # тестовый класс - метод __call__
    transmorph = {("Вода", "Воздух"): "Шторм", ("Вода", "Огонь"): "Пар", ("Вода", "Земля"): "Грязь",
                  ("Воздух", "Огонь"): "Молния", ("Воздух", "Земля"): "Пыль", ("Огонь", "Земля"): "Лава"}

    def __call__(self, *args):
        args_reversed = (args[1], args[0])
        if args in self.transmorph:
            return self.transmorph[args]
        elif args_reversed in self.transmorph:
            return self.transmorph[args_reversed]
        else:
            return None

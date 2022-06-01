class Child:

    def __init__(self, name, age, is_hungry=False, is_calm=True):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
        self.is_calm = is_calm


class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_children(self, *args):
        for arg in args:
            if arg.age <= self.age - 16:
                print("Иди ко мне,", arg.name)
                self.children.append(arg)
            else:
                print("Иди к своей маме,", arg.name)

    def introduce_yourself(self):
        print(f"Я - {self.name}. Мне {self.age} лет. У меня {len(self.children)} детей.")
        for child in self.children:
            print(f"{child.name}, {child.age}")

    def feed_child(self, child):
        child.is_hungry = False
        print(f"{child.name} накормлен")

    def calm_child(self, child):
        child.is_calm = True
        print(f"{child.name} успокоен")

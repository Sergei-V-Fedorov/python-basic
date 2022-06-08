class Property:
    """ Клаcc для описания имущества """
    def __init__(self, worth=1000):
        self.worth = worth

    def calculate_tax(self, tax=10):
        return self.worth * tax / 100


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self, tax=0.1):
        return self.worth * tax / 100


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self, tax=0.5):
        return self.worth * tax / 100


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self, tax=0.2):
        return self.worth * tax / 100

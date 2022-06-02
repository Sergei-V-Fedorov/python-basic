class Property:
    """ Клаcc для описания имущества """
    def __init__(self, worth: int = 1000) -> None:
        self.worth = worth

    def calculate_tax(self, tax: int = 10) -> float:
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
    """Класс расчета налога на загородный дом"""
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self, tax: float = 0.2) -> float:
        return self.worth * tax / 100

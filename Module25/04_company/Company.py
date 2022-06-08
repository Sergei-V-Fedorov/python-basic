class Person:

    def __init__(self, name, surname, age):
        self.set_name(name)
        self.set_surname(surname)
        self.set_age(age)

    def set_name(self, user_name):
        if user_name.isalpha():
            self.__name = user_name.capitalize()
        else:
            raise TypeError("Недопустимое имя")

    def set_surname(self, user_name):
        if user_name.isalpha():
            self.__surname = user_name.capitalize()
        else:
            raise TypeError("Недопустимая фамилия")

    def set_age(self, user_age):
        if 16 <= user_age <= 85:
            self.__age = user_age
        else:
            raise TypeError("Недопустимый возраст")

    def __str__(self):
        return "Имя: {}, фамилия: {}, возраст {}".format(
            self.__name, self.__surname, self.__age
        )

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):
    position = "Служащий"

    def salary(self, wages, bonus=0):
        return wages * bonus / 100

    '''def get_position(self):
        return self.__position'''


class Manager(Employee):
    position = "Менеджер"

    def salary(self, wages=13000):
        return wages


class Agent(Employee):
    position = "Агент"

    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.sale_volume = sales_volume

    def salary(self, wages=5000):
        return wages + self.sale_volume * 0.05


class Worker(Employee):
    position = "Рабочий"

    def __init__(self, name, surname, age, worked_hours):
        super().__init__(name, surname, age)
        self.worked_hours = worked_hours

    def salary(self, wages=100):
        return wages * self.worked_hours

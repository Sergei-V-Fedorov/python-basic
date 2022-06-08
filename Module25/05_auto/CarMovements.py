import math


class Car:
    """Класс автомобиль с некоторыми методами из turtle"""
    def __init__(self, x=0, y=0, angle=0, distance=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.odometer = distance

    def forward(self, distance):
        self.x += distance * math.cos(math.radians(self.angle))
        self.y += distance * math.sin(math.radians(self.angle))
        self.odometer += distance

    def left(self, angle):
        self.angle = (self.angle + angle) % 360

    def right(self, angle):
        self.angle = (360 - self.angle + angle) % 360

    def setheading(self, angle):
        self.angle = angle

    def position(self):
        return round(self.x, 2), round(self.y, 2)

    def heading(self):
        return self.angle

    def __str__(self):
        return "x = {0:.2f},  y = {1:.2f}, пробег = {2:.2f}".format(
            self.x, self.y, self.odometer
        )


class Buss(Car):

    def __init__(self, x=0, y=0, angle=0, distance=0, passengers=0, money=0):
        super().__init__(x, y, angle, distance)
        self.passengers = passengers
        self.money = money

    def come_in(self, count):
        self.passengers += count

    def come_out(self, count):
        if self.passengers >= count:
            self.passengers -= count

    def forward(self, distance):
        self.x += distance * math.cos(math.radians(self.angle))
        self.y += distance * math.sin(math.radians(self.angle))
        self.odometer += distance
        self.money += self.passengers * distance / 10 * 50

    def __str__(self):
        return "x = {0:.2f},  y = {1:.2f}, пробег = {2:.2f}, кол-во пассажиров = {3}, заработано = {4:.2f} руб".format(
            self.x, self.y, self.odometer, self.passengers, self.money)

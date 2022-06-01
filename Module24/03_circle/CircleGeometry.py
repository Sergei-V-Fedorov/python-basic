class Circle:
    pi = 3.141592653589793

    def __init__(self, x, y, radius=1):
        self.centerX = x
        self.centerY = y
        self.radius = radius

    def calc_square(self):
        return self.pi * self.radius**2

    def calc_perimetr(self):
        return 2 * self.pi * self.radius

    def magnify(self, multiplier=1):
        self.radius *= multiplier

    def is_intersected(self, x, y, radius):
        return (x - self.centerX)**2 + (y - self.centerY)**2 <= \
               (radius + self.radius)**2

    def show_info(self):
        print(f"Окружность с координатами центра "
              f"({self.centerX}, {self.centerY}) и радиусом {self.radius}")

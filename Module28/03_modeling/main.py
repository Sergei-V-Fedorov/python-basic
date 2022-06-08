class Square:
    """Класс для реализации квадрата """

    def __init__(self, side: float) -> None:
        self._side = side

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, side: float) -> None:
        self._side = side

    def square(self) -> float:
        """ Вычисляет площадь """
        return self._side ** 2

    def perimeter(self) -> float:
        """ Вычисляет периметр """
        return 4 * self._side

    def __str__(self):
        return f"Квадрат со стороной {self._side}"


class Triangle:
    """Класс для реализации равнобедренного треугольника """

    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def square(self) -> float:
        """ Вычисляет площадь """
        return self.base * self.height / 2

    def perimeter(self) -> float:
        """ Вычисляет периметр """
        return 2 * (self.height**2 + (self.base / 2)**2)**0.5 + self.base

    def __str__(self):
        return f"Треугольник с основанием {self.base} и высотой {self.height}"


class Figure:
    """ Базовый класс для фигур пространственной геометрии """

    def __init__(self) -> None:
        """ Список поверхностей """
        self.surfaces = []

    def square(self) -> float:
        """ Вычисление площади всех поверхностей """
        result = [surface.square() for surface in self.surfaces]
        return sum(result)


class Cube(Figure):
    """Класс для реализации куба """

    def __init__(self, element: Square) -> None:
        super().__init__()
        self.surfaces = [element for _ in range(6)]


class Pyramid(Figure):
    """Класс для реализации пирамиды """

    def __init__(self, element_1: Square, element_2: Triangle) -> None:
        super().__init__()
        self.surfaces = [element_2 for _ in range(4)]
        self.surfaces.append(element_1)


square = Square(2)
print(square)
print("Периметр квадрата:", square.perimeter())
print("Площадь квадрата:", square.square())

# Создаем куб
cube = Cube(square)
cube_surfaces_square = cube.square()
print("Площадь поверхности куба", cube_surfaces_square)

print()
# создаем треугольник
triangle = Triangle(base=2, height=6)
print(triangle)
print("Периметр треугольника", triangle.perimeter())
print("Площадь треугольника", triangle.square())

# Создаем пирамиду
pyramid = Pyramid(square, triangle)
pyramid_surfaces_square = pyramid.square()
print("Площадь поверхности пирамиды", pyramid_surfaces_square)

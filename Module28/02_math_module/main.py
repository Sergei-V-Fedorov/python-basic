class MyMath:
    """
    Реализует методы для вычисления некоторых геометрических характеристик
    """
    __pi = 3.141592654

    @classmethod
    def circle_len(cls, radius: float = 1) -> float:
        """ Вычисление длины окружности """
        return 2 * cls.__pi * radius

    @classmethod
    def circle_sq(cls, radius: float = 1) -> float:
        """ Вычисление площади круга """
        return cls.__pi * radius ** 2

    @classmethod
    def sphere_sq(cls, radius: float = 1) -> float:
        """ Вычисление площади сферы """
        return 4 * cls.__pi * radius ** 2

    @classmethod
    def cube_vol(cls, side: float = 1) -> float:
        """ Вычисление объема куба """
        return side ** 3


circle_length = MyMath.circle_len(radius=5)
circle_square = MyMath.circle_sq(radius=6)
print("Длина окружности:", circle_length)
print("Площадь круга:", circle_square)
cube_volume = MyMath.cube_vol(side=5)
print("Объем куба:", cube_volume)
sphere_square = MyMath.sphere_sq(radius=6)
print("Площадь поверхности сферы:", sphere_square)

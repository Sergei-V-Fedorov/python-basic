from CircleGeometry import Circle

# 1ая окружность S=pi, P=2*pi, 2ая S=78.5, P=31.4, 3ья S=314, P=62.8
# 2ая и 3ья окружность пересекаются,
# 1ая со 2ой и 3ей - не пересекается. После увеличения в 20 раз пересекается со 2ой

geometry = [(0, 0, 1), (10, 20, 5), (25, 20, 10)]
circles = []

# заполняем
for x, y, radius in geometry:
    one_circle = Circle(x, y, radius)
    circles.append(one_circle)

# проверяем
for one_circle in circles:
    one_circle.show_info()
    print("Площадь =", one_circle.calc_square())
    print("Периметр =", one_circle.calc_perimetr())

print()
if circles[0].is_intersected(circles[1].centerX, circles[1].centerY, circles[1].radius):
    print("Первая окружность пересекается со второй")
else:
    print("Первая окружность НЕ пересекается со второй")

print("\nУвеличиваем первую окружность в 20 раз")
circles[0].magnify(20)
circles[0].show_info()
print("Площадь =", circles[0].calc_square())
print("Периметр =", circles[0].calc_perimetr())

print("А теперь пересекается?")
if circles[0].is_intersected(circles[1].centerX, circles[1].centerY, circles[1].radius):
    print("Первая окружность пересекается со второй")
else:
    print("Первая окружность НЕ пересекается со второй")

print()
if circles[2].is_intersected(circles[1].centerX, circles[1].centerY, circles[1].radius):
    print("Вторая окружность пересекается с третьей")
else:
    print("Вторая окружность НЕ пересекается с третьей")

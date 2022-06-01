def search(x, y, r):
    if x * x + y * y - r * r <= 1e-36:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")

print("Введите координаты монетки:")
x = float(input("X: "))
y = float(input("Y: "))
r = float(input("Введите радиус: "))

search(x, y, r)

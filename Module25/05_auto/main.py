import CarMovements as cm

zaporozhec = cm.Car()

print("Начинаем движение\n", zaporozhec)
zaporozhec.left(90)
zaporozhec.forward(10)
print(zaporozhec)

zaporozhec.right(45)
zaporozhec.forward(200**0.5)  # sqrt(10**2 + 10**2)
print(zaporozhec)

zaporozhec.left(135)
zaporozhec.forward(10)
print(zaporozhec)

zaporozhec.right(45)
zaporozhec.forward(200**0.5)  # sqrt(10**2 + 10**2)
print(zaporozhec)

zaporozhec.setheading(180)
zaporozhec.forward(20)

print("Конечная", zaporozhec.position())

# ----------------------
icarus = cm.Buss()

print("\nНачинаем движение\n", icarus)
icarus.left(90)
icarus.come_in(3)
icarus.forward(10)
print(icarus)

icarus.come_out(1)
icarus.come_in(2)
icarus.right(45)
icarus.forward(200**0.5)  # sqrt(10**2 + 10**2)
print(icarus)

icarus.come_out(2)
icarus.come_in(1)
icarus.left(135)
icarus.forward(10)
print(icarus)

icarus.come_out(1)
icarus.come_in(3)
icarus.right(45)
icarus.forward(200**0.5)  # sqrt(10**2 + 10**2)
print(icarus)

icarus.setheading(180)
icarus.forward(20)

print("Конечная", icarus.position())

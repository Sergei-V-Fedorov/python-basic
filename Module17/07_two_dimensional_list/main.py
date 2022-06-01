upper = 9  # слагаемое для вычисления верхней границы range()
step = 4  # шаг для range()
length = 4  # размерность массива

array_2d = [[column for column in range(row, row + upper, step)] for row in range(1, length + 1)]

print("Двумерный список:", array_2d)

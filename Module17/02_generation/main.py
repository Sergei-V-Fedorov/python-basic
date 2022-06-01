length = int(input("Введите длину списка: "))

result = [1 if not number % 2 else number % 5 for number in range(length)]

print("Результат:", result)

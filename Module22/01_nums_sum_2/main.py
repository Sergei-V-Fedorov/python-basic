with open("numbers.txt", 'r') as text_file:
    numbers = text_file.read()

# вывод содержимого файла
print("Содержимое файла numbers.txt")
print(numbers)

# подсчет суммы
numbers = map(int, numbers.split())
summa = sum(numbers)
print("\nСодержимое файла answer.txt")
print(summa)

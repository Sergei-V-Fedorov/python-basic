import random

max_number = int(input("Введите максимальное число: "))

secret_number = random.randint(1, max_number)
print("загадал", secret_number)
possible_numbers = set()

while True:
    sequence = input("\nНужное число есть среди вот этих чисел: ")
    if sequence == "Помогите!":
        print("Артём мог загадать следующие числа:", *possible_numbers)
        break
    sequence = map(int, sequence.split())
    sequence = set(sequence)
    if secret_number in sequence:  # есть среди названных
        print("Ответ Артёма: Да")
        possible_numbers.update(sequence)  # добавляем в множество
    else:  # нет среди названных
        print("Ответ Артёма: Нет")
        possible_numbers -= sequence  # вычитаем из множества
    if len(possible_numbers) == 1:  # угадали
        print("\nУгадали! Загаданное число:", *possible_numbers)
        break

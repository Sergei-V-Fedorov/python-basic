quantity = int(input("Кол-во человек: "))
number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number}-й человек")

people = list(range(1, quantity + 1))
start_index = 0

while len(people) > 1:
    print("\nТекущий круг людей:", people)
    print("Начало счёта с номера", people[start_index])
    start_index += number % len(people) - 1
    dropped = people[start_index]
    print("Выбывает человек под номером", dropped)
    people.remove(dropped)
    start_index %= len(people)

print("\nОстался человек под номером", *people)

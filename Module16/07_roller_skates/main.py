# Заполняем список размеров коньков
quantity = int(input("Кол-во коньков: "))
skate_sizes = []
for number in range(quantity):
    size = int(input(f"Размер {number + 1}-й пары: "))
    skate_sizes.append(size)

# Заполняем список размеров ног
people = int(input("\nКол-во людей: "))
foot_sizes = []
for number in range(people):
    size = int(input(f"Размер ноги {number + 1}-го человека: "))
    foot_sizes.append(size)

# берем размер ноги/ смотрим наличие коньков/ удаляем, если есть / увеличиваем счетчик
count = 0
for size in foot_sizes:
    if size in skate_sizes:
        count += 1
        skate_sizes.remove(size)

print("\nНаибольшее кол-во людей, которые могут взять ролики:", count)

quantity = int(input("Кол-во друзей: "))
debt = int(input("Долговых расписок: "))

# запишем все суммы во вложенный массив, потом просуммируем
friends_bills = [[0] for number in range(quantity)]
for number in range(debt):
    print(f"\n{number + 1}-я расписка")
    debtor = int(input("Кому: "))
    lender = int(input("От кого: "))
    amount = int(input("Сколько: "))
    friends_bills[debtor - 1].append(-amount)
    friends_bills[lender - 1].append(amount)

print("\nБаланс друзей:")
for index in range(len(friends_bills)):
    total = sum(friends_bills[index])
    print(f"{index + 1}: {total}")

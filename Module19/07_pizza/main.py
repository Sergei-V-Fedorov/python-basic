order_quantity = int(input("Введите количество заказов: "))

pizza_time_db = {}
for index in range(order_quantity):
    order = input(f"{index + 1}-й заказ: ").split()
    name, pizza, quantity = tuple(order)
    quantity = int(quantity)

    if name in pizza_time_db:  # клиент в БД
        if pizza in pizza_time_db[name]:  # повторная покупка пиццы
            pizza_time_db[name][pizza] += quantity
        else:  # новая пицца
            pizza_time_db[name].update({pizza: quantity})
    else:  # нет в БД
        pizza_time_db[name] = {pizza: quantity}

print()
for name in sorted(pizza_time_db):
    print(f"{name}:")
    for pizza in sorted(pizza_time_db[name]):
        print(f"\t{pizza}: {pizza_time_db[name][pizza]}")

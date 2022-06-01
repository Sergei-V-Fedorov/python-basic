goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for name_good, code_good in goods.items():
    length = len(store[code_good])
    total_quantity = 0
    total_price = 0

    for index in range(length):
        quantity = store[code_good][index]["quantity"]
        price = store[code_good][index]["price"]
        total_quantity += quantity
        total_price += price * quantity

    print(f"{name_good} - {total_quantity} штук, стоимость {total_price} руб")

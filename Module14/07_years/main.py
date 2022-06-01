def inrange(x, low, high):  # провка low <= x <= high
    return low <= x <= high


def triple_numbers(year1, year2):  # генерация годов, используя цифры 2-х старших разрядов ab??
    low = year1 // 100
    high = year2 // 100 + 1
    years = []
    for i in range(low, high + 1):
        decim, units = i // 10, i % 10
        # генерируем года X?XX and ?XXX
        for year in (i * 100 + decim * 10 + decim, i * 100 + units * 10 + units):
            if inrange(year, year1, year2):  # проверка на вхождение в диапазон
                years += [year]

    years.sort()
    print(*years, sep='\n')

year1 = int(input("Введите первый год: "))
year2 = int(input("Введите второй год: "))
year1, year2 = min(year1, year2), max(year1, year2)  # проверка/перестановка

triple_numbers(year1, year2)

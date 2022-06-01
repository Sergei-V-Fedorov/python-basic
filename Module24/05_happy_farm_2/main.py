import Garden

gardener_1 = Garden.Gardener("Пафнутий")  # садовник
my_garden_1 = Garden.PotatoGarden(5)  # грядка из 5 кустов картошки
my_garden_2 = Garden.PotatoGarden(10)  # грядка из 10 кустов картошки
gardener_1.add_garden(my_garden_1, my_garden_2)  # добавили задание садовнику 1

for index, garden in enumerate(gardener_1.gardens, start=1):
    print(f"На грядке {index} ", end='')  # начальное состояние урожая

    if index == 1:  # будем ухаживать усердно
        for _ in range(3):
            gardener_1.take_care(index - 1)  # позаботиться

        gardener_1.take_harvest(index - 1)  # собрать урожай

    elif index == 2:  # будем ухаживать по настроению
        for _ in range(2):
            gardener_1.take_care(index - 1)  # позаботиться

        gardener_1.take_harvest(index - 1)  # собрать урожай

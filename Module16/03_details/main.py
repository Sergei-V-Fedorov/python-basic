shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input("Название детали: ")


# подсчет кол-ва наименований в списке и их суммарной стоимости
def search(price_list, item_name):
    # список цен товара item_name
    result = [item[1] for item in price_list if item[0] == item_name]
    return len(result), sum(result)


count, total_price = search(shop, detail)

print("Кол-во деталей —", count)
print("Общая стоимость —", total_price)

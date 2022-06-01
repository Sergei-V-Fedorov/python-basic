# поиск ключа в словаре с уровнем вложенности
def find_key_in_dict(dict_for_search, key_for_search, nest_level=-1):
    result = None
    if nest_level == 0:  # отработает при nest_level == 0
        return result
    if key_for_search in dict_for_search:  # отработает при nest_level == 1
        return dict_for_search[key_for_search]

    nest_level -= 1  # каждый рекурсивный вызов уменьшает уровень вложенности

    for element in dict_for_search.values():
        if isinstance(element, dict):
            result = find_key_in_dict(element, key_for_search, nest_level)
            if result:
                break

    return result  # отрабатывает, когда ключ вложенности по-умолчанию


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


key = input("Введите искомый ключ: ")
request = input("Хотите ввести максимальную глубину? Y/N: ").lower()
if request == 'y':
    max_depth = int(input("Введите максимальную глубину: "))
    value = find_key_in_dict(site, key, max_depth)
else:
    value = find_key_in_dict(site, key)

print("Значение ключа:", value)

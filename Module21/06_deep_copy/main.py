# рекурсивное разворачивание словаря
def new_recursion(user_dict, level=0):
    if level == 0:
        print("site = {\n" + new_recursion(user_dict, level + 1) + "\n}")
    else:
        string_1 = ""
        length = len(user_dict)
        for key, value in user_dict.items():
            comma = ",\n" if length > 1 else ""  # запятая
            tab = '\t' * level  # отступ
            string_1 += "{0:}'{1:}': ".format(tab, key)

            length -= 1
            if isinstance(value, dict):
                string_1 += "{\n" + \
                            new_recursion(value, level + 1) + \
                            "\n{0}{1}".format(tab, '}') + comma
            else:
                string_1 += "'{0}'".format(value) + comma
        return string_1


site = {
        'html': {
            'head': {
                'title': 'Куплю/продам телефон недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на iphone',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }


number_sites = int(input("Сколько сайтов: "))
for index in range(number_sites):
    product = input("\nВведите название продукта для нового сайта: ")
    print(f"Сайт для {product}:")

    substring_1 = f"Куплю/продам {product} недорого"
    substring_2 = f"У нас самая низкая цена на {product}"
    site["html"]["head"]["title"] = substring_1
    site["html"]["body"]["h2"] = substring_2

    new_recursion(site)
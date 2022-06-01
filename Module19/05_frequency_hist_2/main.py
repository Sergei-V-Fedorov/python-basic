# подсчет кол-ва символов в тексте
def histogram(original_text):
    result = dict.fromkeys(original_text)
    for key_1 in result:
        result[key_1] = original_text.count(key_1)
    return result


# меняет местами ключи и значения
def reverse_dictionary(original_dict):
    result = {}
    for key_1, value_1 in original_dict.items():
        if value_1 in result:
            result[value_1].append(key_1)
        else:
            result[value_1] = [key_1]
    return result


text = input("Введите текст: ")

original_frequency = histogram(text)
print("Оригинальный словарь частот:")
for key in sorted(original_frequency):
    print(f"{key} : {original_frequency[key]}")

reversed_frequency = reverse_dictionary(original_frequency)
print("\nИнвертированный словарь частот:")
for key in sorted(reversed_frequency):
    print(f"{key} : {reversed_frequency[key]}")

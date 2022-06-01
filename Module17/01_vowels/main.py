vowels = 'аиеёоуыэюя'


# выбор букв из template и их количество
def select_vowels(source_text, template):
    result = [letter for letter in source_text if letter in template]
    length = len(result)
    return result, length


text = input("Введите текст: ")

only_vowels, amount = select_vowels(text, vowels)

print("Список гласных букв:", only_vowels)
print("Длина списка:", amount)

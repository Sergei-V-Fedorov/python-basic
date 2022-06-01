# переворачивает строку, сохраняя позицию пунктуации
def reverse_on_punctuation(original_string):
    copy_of_original = original_string[:] + '\0'  # для отслеживания конца строки
    string_of_letters = []
    result = []
    for symbol in copy_of_original:
        if symbol.isalpha():  # формируем слово
            string_of_letters.append(symbol)  # добавляем в слово
        elif not symbol.isalpha() or symbol == '\0':  # добавляем слово в резалт
            reversed_word = ''.join(string_of_letters[::-1])  # переворачиваем слово,
            result.append(reversed_word + symbol)  # добавляем в резалт вместе с пунктуацией
            string_of_letters = []
    result = ''.join(result)
    return result[:-1]   # без '\0'


message = input("Сообщение: ").split()
new_message = []

for word in message:
    if word.isalpha():  # не содержит пунктуации
        new_message.append(word[::-1])  # переворачиваем строку
    else:  # содержит пунктуацию
        revered_word = reverse_on_punctuation(word)  # переворачиваем строку с учетом пунктуации
        new_message.append(revered_word)

new_message = ' '.join(new_message)

print("\nНовое сообщение:", new_message)


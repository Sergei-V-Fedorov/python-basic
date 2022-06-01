rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

original_text = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
length = len(rus_lower_alphabet)

coded_text = []
for symbol in original_text.lower():
    if symbol in rus_lower_alphabet:
        index = (rus_lower_alphabet.index(symbol) + shift) % length
        coded_symbol = rus_lower_alphabet[index]
    else:
        coded_symbol = symbol
    coded_text.append(coded_symbol)

coded_text = ''.join(coded_text)

print("Зашифрованное сообщение:", coded_text)

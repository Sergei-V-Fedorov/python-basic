text = input("Введите строку: ")

text += '\0'  # дополним стоку для удобства
previous_symbol = text[0]
count = 0
compressed_text = []

for symbol in text:
    if symbol != previous_symbol:
        compressed_text.extend([previous_symbol, str(count)])
        previous_symbol = symbol
        count = 1
    else:
        count += 1

compressed_text = ''.join(compressed_text)

print("\nЗакодированная строка:", compressed_text)

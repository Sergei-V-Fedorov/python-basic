import string
import os


# вывод на печать содержимого файла
def print_text_file(target):
    short_name = os.path.split(target)
    with open(target, 'r') as text_file:
        user_text = text_file.read()
    print(f"Содержимое файла '{short_name[1]}':")
    print(user_text)


# возвращает строку со сдвигом
def caesar_cipher(coded_string, cypher_shift):
    result = []
    length_1 = len(string.ascii_lowercase)
    length_2 = len(string.punctuation)
    for symbol in coded_string:
        if symbol.lower() in string.ascii_lowercase:  # переставляем буквы
            ind = (string.ascii_lowercase.index(symbol.lower()) + cypher_shift) % length_1
            coded_symbol = string.ascii_lowercase[ind]
            if symbol.isupper():
                coded_symbol = coded_symbol.upper()
        elif symbol in string.punctuation:  # переставляем символы
            ind = (string.punctuation.index(symbol) + cypher_shift) % length_2
            coded_symbol = string.punctuation[ind]
        else:
            coded_symbol = symbol
        result.append(coded_symbol)
    return ''.join(result)


with open('text.txt', 'r') as input_file:  # прочитали текст
    text = input_file.readlines()

with open('cipher_text.txt', 'w') as output_file:  # закодировали и записали
    for index, line in enumerate(text, start=1):
        coded_text = caesar_cipher(line, index)
        output_file.write(coded_text)

print_text_file('text.txt')  # вывод на печать
print()
print_text_file('cipher_text.txt')

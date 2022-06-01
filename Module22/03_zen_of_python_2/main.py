import os
import string


# словарь для подсчета букв в тексте
def letters_counter(user_dict, user_text):
    unique_keys = set(user_text)
    for key_1 in unique_keys:
        if key_1 in string.ascii_letters:
            if key_1 in user_dict:
                user_dict[key_1] += user_text.count(key_1)
            else:
                user_dict[key_1] = user_text.count(key_1)


# словом считаем комбинацию символов, разделенных пробелами, т.к. другое не оговаривается
# прописные и строчные буквы считаются одной буквой, иначе самую редкую не найдем
input_file = os.path.join("..", "02_zen_of_python", "zen.txt")
with open(input_file, 'r') as text_file:
    number_strings = 0
    number_words = 0
    latin_letters = {}
    for line in text_file.readlines():
        # кол-во строк
        number_strings += 1
        # кол-во букв в словах
        letters_counter(latin_letters, line.lower())
        # кол-во слов в строке
        line = line.split()
        number_words += len(line)

number_letters = list(latin_letters.values())   # подсчет кол-ва букв
number_letters = sum(number_letters)

# подсчет частоты букв и сортировка
letter_frequency = [(key, value) for key, value in latin_letters.items()]  # список из (key, value)
letter_frequency = sorted(letter_frequency, key=lambda item: item[1])
rarest_letter = letter_frequency[0][0]

print("Количество букв в файле:", number_letters)  #652
print("Количество слов в файле:", number_words)  # 137
print("Количество строк в файле:", number_strings)  # 19
print("Наиболее редкая буква:", rarest_letter)  # k - 2 раза

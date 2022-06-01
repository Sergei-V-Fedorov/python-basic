import os
import string


# словарь для подсчета букв в тексте
def letters_counter(user_dict, user_text):
    unique_keys = set(user_text)
    for key_1 in unique_keys:
        if key_1 in string.ascii_lowercase:
            if key_1 in user_dict:
                user_dict[key_1] += user_text.count(key_1)
            else:
                user_dict[key_1] = user_text.count(key_1)


# вывод на печать содержимого файла
def print_text_file(target):
    short_name = os.path.split(target)
    with open(target, 'r') as tfile:
        user_text = tfile.read()
    print(f"Содержимое файла '{short_name[1]}':")
    print(user_text)


# формирует файл с результатами анализа
def write_protocol(analysis_report, user_analysis):
    total_letters = sum(user_analysis.values())

    protocol_results = sorted(user_analysis.items(), key=lambda record: (-record[1], record[0]))

    with open(analysis_report, 'w') as ofile:
        for letter, amount in protocol_results:
            new_record = "{0} {1:.3f}\n".format(letter, amount / total_letters)
            ofile.write(new_record)


file_name = "text.txt"
output_file = "analysis.txt"

if os.path.exists(file_name):
    print_text_file(file_name)  # печать исходного файла
    print()

    with open(file_name, 'r') as text_file:  # считывание исходного файла
        text = text_file.read()

    analysis_result = {}
    letters_counter(analysis_result, text.lower())  # подсчет букв

    write_protocol(output_file, analysis_result)  # запись частотного анализа
    print_text_file(output_file)  # печать результатов из файла
else:
    print(f"Файл '{file_name}' не найден")

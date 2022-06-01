import os
import string
import zipfile


RUS_ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


# словарь для подсчета букв в тексте
def letters_counter(user_dict, user_text):
    unique_keys = set(user_text)
    for key_1 in unique_keys:
        if key_1 in string.ascii_letters or key_1 in RUS_ALPHABET:
            if key_1 in user_dict:
                user_dict[key_1] += user_text.count(key_1)
            else:
                user_dict[key_1] = user_text.count(key_1)


# формирует файл с результатами анализа
def write_protocol(analysis_report, user_analysis):
    protocol_results = sorted(user_analysis.items(), key=lambda record: (-record[1], record[0]))

    with open(analysis_report, 'w') as ofile:
        for letter, amount in protocol_results:
            new_record = "{0} {1}\n".format(letter, amount)
            ofile.write(new_record)


# вывод на печать содержимого файла
def print_text_file(target):
    short_name = os.path.split(target)
    with open(target, 'r') as tfile:
        user_text = tfile.read()
    print(f"Содержимое файла '{short_name[1]}':")
    print(user_text)


zip_file_name = "voyna-i-mir.zip"
output_file = "analysis.txt"

if os.path.exists(zip_file_name):
    # разархивирование
    with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
        file_name = zip_file.namelist()[0]
        zip_file.extract(file_name)

    analysis_result = {}  # подсчет кол-ва букв
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding="UTF-8") as text:
            count = 0
            for line in text:
                letters_counter(analysis_result, line)
                count += 1

        write_protocol(output_file, analysis_result)  # запись в файл

        #print_text_file(output_file)  # вывод файла
    else:
        print(f"Файл '{file_name}' не разархивирован")
else:
    print(f"Файл '{zip_file_name}' не найден")

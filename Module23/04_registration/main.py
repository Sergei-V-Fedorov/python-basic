registration_log = "registrations.txt"
correct_log = "registrations_good.log"
wrong_log = "registrations_bad.log"


# валидация данных
def validation_info(data):
    result = ""  # если валидные данные, иначе текст исключения
    try:
        if len(data) != 3:
            raise IndexError
        if not data[0].isalpha():
            raise NameError()
        if '.' not in data[1] and '@' not in data[1]:
            raise SyntaxError()
        if int(data[2]) < 10 or int(data[2]) > 99:
            raise ValueError
    except ValueError:
        result = "Поле 'Возраст' НЕ является числом от 10 до 99"
    except SyntaxError:
        result = "Поле 'e-mail' НЕ содержит '@' и '.'"
    except NameError:
        result = "Поле имени содержит НЕ только буквы"
    except IndexError:
        result = "НЕ присутствуют все три поля"
    finally:
        return result


# считывание логов регистрации
def read_registration_log(log_file):
    with open(log_file, 'r') as tf:
        result = [line.split() for line in tf]
    return result


registration_data = read_registration_log(registration_log)  # логи регистрации

correct_record = open(correct_log, 'w')
wrong_record = open(wrong_log, 'w')

for user_data in registration_data:
    validation = validation_info(user_data)  # получаем текст исключения
    if not validation:
        correct_record.write(' '.join(user_data) + '\n')
    else:
        wrong_record.write(' '.join(user_data) + '\t' + validation + '\n')

correct_record.close()
wrong_record.close()

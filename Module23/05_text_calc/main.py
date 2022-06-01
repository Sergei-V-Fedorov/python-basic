OPERATORS = ['+', '-', '*', '/', "//", '%']


#  формирует сообщение об ошибке
def repair_message(user_calc):
    temporary = user_calc.split()
    try:
        if len(temporary) != 3:
            raise IndexError
        if not (isinstance(int(temporary[0]), int) and isinstance(int(temporary[2]), int)):
            raise ValueError
        if temporary[1] not in OPERATORS:
            raise SyntaxError
        return ""
    except ValueError:
        return "Операнды должны быть целыми числами"
    except IndexError:
        return "Неверный формат строки: ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделённые пробелами"
    except SyntaxError:
        return "Доступные операции: " + ', '.join(OPERATORS)


operations = "calc.txt"

total = []
with open(operations, 'r') as ifile:
    for line in ifile:
        while True:
            message = repair_message(line)
            if not message:  # правильно
                try:
                    calc_result = eval(line)
                    total.append(calc_result)
                    break
                except ZeroDivisionError:
                    print("Делить на нуль нельзя!")
                    break
            else:  # неправильно
                print("Обнаружена ошибка в строке:", line)
                print(message)
                answer = input("Хотите исправить (Да/Нет)? ").lower()
                if answer == "нет":
                    break
                else:
                    line = input("Введите исправленную строку: ")

print("\nСумма результатов:", sum(total))

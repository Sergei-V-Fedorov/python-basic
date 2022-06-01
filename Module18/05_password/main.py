# проверка на заглавные буквы
def check_for_capital(word_for_check):
    upper_letters = [symbol.isupper() for symbol in word_for_check]
    result = any(upper_letters)
    return result


# проверка на кол-во цифр
def check_for_digit(word_for_check):
    digits_in_word = [symbol.isdigit() for symbol in word_for_check]
    number_of_digits = sum(digits_in_word)
    result = number_of_digits >= 3
    return result


while True:
    password = input("Придумайте пароль: ")

    if len(password) >= 8 and check_for_capital(password) and check_for_digit(password):
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")

ip_address = input("Введите IP: ")

if ip_address.count('.') != 3:  # проверка на кол-во цифр
    print("Адрес — это четыре числа, разделённые точками.")
else:
    ip_address = ip_address.split('.')

    digits_position = [word.isdigit() for word in ip_address]
    if not all(digits_position):  # проверка на цифры
        for number, position in zip(ip_address, digits_position):
            if not position:
                print(f"{number} — это не целое число.")
    else:
        digit_limit = [int(word) < 256 for word in ip_address]
        if not all(digit_limit):  # проверка на величину цифр
            for number, value in zip(ip_address, digit_limit):
                if not value:
                    print(f"{number} превышает 255.")
        else:
            print("IP-адрес корректен.")

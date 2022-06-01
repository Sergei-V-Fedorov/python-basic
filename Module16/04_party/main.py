guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def go_back(guest_list, guest_name):  # гость уходит
    if guest_name in guest_list:
        guest_list.remove(guest_name)
    print(f"Пока, {guest_name}!\n")


def come_in(guest_list, guet_name):  # гость приходит
    if len(guest_list) < 6:
        guest_list.append(guet_name)
        print(f"Привет, {guet_name}!\n")
    else:
        print(f"Прости, {guet_name}, но мест нет.\n")


while True:
    print(f"Сейчас на вечеринке {len(guests)} человек:", guests)
    request = input("Гость пришёл или ушёл? ")
    if request == "Пора спать":
        print("\nВечеринка закончилась, все легли спать.")
        break
    name = input("Имя гостя: ")
    if request == "ушёл":
        go_back(guests, name)
    elif request == "пришёл":
        come_in(guests, name)

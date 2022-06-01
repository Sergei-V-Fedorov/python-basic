def send_message(chat_log, nick_name, user_message):
    try:
        with open(chat_log, 'a') as tf:
            tf.write(f"[{nick_name}]: {user_message}\n")
    except:
        print("Чат временно не доступен. Попробуйте снова")


def show_message(chat_log):
    try:
        with open(chat_log, 'r') as tf:
            text = tf.read()
        print(text)
    except:
        print("Чат временно не доступен. Попробуйте снова")

print("============ ВЫ ЗАШЛИ В ЧАТ NONAME =============")

user_name = input("Введите свое имя: ")
chat_name = "chat_log.txt"

while True:
    print(f"{user_name}, выберете одно из действий:\n"
          f"\t\t1. Посмотреть текущий текст чата\n"
          f"\t\t2. Отправить сообщение\n"
          f"\t\t3. Выход из чата")

    user_choice = input(f"[{user_name}]: ")
    if user_choice in ('1', '2', '3'):

        if user_choice == '3':
            print(f"До встречи, {user_name}!")
            break
        elif user_choice == '2':
            message = input(f"[{user_name}]: ")
            send_message(chat_name, user_name, message)
        elif user_choice == '1':
            print(user_choice)
            show_message(chat_name)

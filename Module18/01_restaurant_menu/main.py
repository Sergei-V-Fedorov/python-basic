menu_original = input("Доступное меню: ")
menu_parsed = menu_original.split(';')
menu_parsed = ', '.join(menu_parsed)

print("\nНа данный момент в меню есть:", menu_parsed)

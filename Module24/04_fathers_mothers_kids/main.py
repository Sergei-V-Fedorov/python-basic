import Family

Valya = Family.Parent("Валентина", 35)

Petya = Family.Child("Петя", 28, is_hungry=True)

Dima = Family.Child("Дима", 10, is_hungry=True)

Olya = Family.Child("Оля", 7, is_calm=False)

Platon = Family.Child("Платон", 2, is_calm=False, is_hungry=True)

children = [Platon, Olya, Dima, Petya]

# добавляем детей
Valya.add_children(*children)
print()
# представься
Valya.introduce_yourself()
print()
# покормить и успокоить
for child in Valya.children:
    if child.is_hungry:
        Valya.feed_child(child)
    if not child.is_calm:
        Valya.calm_child(child)
print()  # проверка
hungry = [not child.is_hungry for child in Valya.children]
calm = [child.is_calm for child in Valya.children]
if all(hungry):
    print("Все сыты", end='')
    if all(calm):
        print(" и довольны")

number_people = int(input("Введите количество человек: "))

pairs = {}
for index in range(number_people - 1):
    pair = input(f"{index + 1}-я пара: ").split()
    descendant, ancestor = tuple(pair)
    if ancestor in pairs:
        pairs[ancestor].append(descendant)
    else:
        pairs[ancestor] = [descendant]

# словарь для тестов
'''pairs = {'Peter_I': ['Alexei', 'Anna', 'Elizabeth'],
         'Alexei': ['Peter_II'],
         'Anna': ['Peter_III'],
         'Peter_III': ['Paul_I'],
         'Paul_I': ['Alexander_I', 'Nicholaus_I']}'''

# определяем родоначальника = его нет в потомках
patriarch = None
all_descendant = []  # все потомки
for descendant in pairs.values():
    all_descendant.extend(descendant)
for ancestor in pairs:  # если нет в потомках, то родоначальник
    if ancestor not in all_descendant:
        patriarch = ancestor
        break

family_tree = {patriarch: 0}  # заполняем родовое дерево

parents = [patriarch]  # список родителей

# Для родителей ищем детей. Детей заносим в список новых родителей. Пока список родителей не опустеет
while parents:
    new_parents = []  # новые родители
    for parent in parents:
        if parent in pairs:  # если оставили детей
            for child in pairs[parent]:  # перебор детей
                family_tree[child] = family_tree[parent] + 1  # заносим ребенка в дерево, увеличивая его высоту
                new_parents.append(child)  # эти дети дадут потомство
    parents = new_parents

print("\n«Высота» каждого члена семьи:")
for name in sorted(family_tree):
    print(name, family_tree[name])

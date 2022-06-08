import Company

monster_corporation = []

for _ in range(1):  # менеджеры
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = int(input("Введите возраст: "))
    manager = Company.Manager(name, surname, age)
    monster_corporation.append(manager)

for _ in range(1):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = int(input("Введите возраст: "))
    volume = int(input("Введите объем продаж: "))
    agent = Company.Agent(name, surname, age, volume)
    monster_corporation.append(agent)

for _ in range(1):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = int(input("Введите возраст: "))
    hours = int(input("Введите кол-во отработанных часов: "))
    worker = Company.Worker(name, surname, age, hours)
    monster_corporation.append(worker)

for employee in monster_corporation:
    print(employee.position)
    print(employee)
    print("Заработная плата", employee.salary())

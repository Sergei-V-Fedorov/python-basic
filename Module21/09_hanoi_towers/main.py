def move(n, x, y):
    if n == 1:
        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(n, x, y))
    else:
        temp = 6 - x - y  # 6 - сумма столбцов
        move(n - 1, x, temp)
        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(n, x, y))
        move(n - 1, temp, y)


n_disks = int(input("Введите количество дисков: "))
move(n_disks, 1, 3)

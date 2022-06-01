with open("zen.txt", 'r') as text_file:
    numbers = text_file.readlines()

numbers[-1] += '\n'  # добавляем перенос строки в последнюю строку

print(*numbers[::-1], sep='')

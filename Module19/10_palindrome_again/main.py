import itertools

text = input("Введите строку: ")
permutations = itertools.permutations(text, len(text))
permutations = [''.join(word) for word in permutations]

for word in permutations:
    if word == word[::-1]:
        print("Можно сделать палиндромом")
        break
else:
    print("Нельзя сделать палиндромом")

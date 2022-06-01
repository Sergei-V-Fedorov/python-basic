number_words = int(input("Введите количество пар слов: "))

vocabulary = {}
for index in range(number_words):
    pair_words = input(f"{index + 1}-я пара: ").split()
    vocabulary[pair_words[0].lower()] = pair_words[-1].lower()

reversed_vocabulary = {value: key
                       for key, value in vocabulary.items()}

vocabulary.update(reversed_vocabulary)

while True:
    request = input("\nВведите слово: ").lower()
    synonym = vocabulary.get(request)
    if synonym is None:
        print("Такого слова в словаре нет.")
    else:
        print("Синоним:", vocabulary[request].capitalize())
        break

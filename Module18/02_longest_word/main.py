text = input("Введите строку: ")
parsed_text = text.split()
parsed_text.sort(key=len, reverse=True)
longest_word = parsed_text[0]
length = len(longest_word)

print("Самое длинное слово:", longest_word)
print("Длина этого слова:", length)

text = input("Введите строку: ")

letter = 'h'

first_index = text.index(letter)
last_index = -1 - text[::-1].index(letter)

print("Развёрнутая последовательность между первым и последним h:",
      text[first_index+1 : last_index][::-1])

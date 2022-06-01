original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# вариант через zip
zip_obj = zip(original_list, original_list[1:])
result = [pair
          for index, pair in enumerate(zip_obj)
          if not index % 2]
print("Новый список (вариант 1):", result)

# через range
result = [(original_list[index], original_list[index + 1])
          for index in range(0, len(original_list), 2)]
print("Новый список (вариант 2):", result)

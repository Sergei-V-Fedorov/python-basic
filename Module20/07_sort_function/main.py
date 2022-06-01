# сортировка кортежа из целых чисел
def sort_tuple_integers(original_tuple):
    if all(isinstance(tuple_item, int)
           for tuple_item in original_tuple):
        return sorted(original_tuple)
    else:
        return original_tuple


# тест секция
'''sequence_1 = (6, 3, -1, 8, 4, 10, -5)
sequence_2 = (6, 3, -1., 8, 4, 10, -5)
sequence_3 = (6, 'a', -5)

print("Ответ в консоли:", sort_tuple_integers(sequence_3))'''

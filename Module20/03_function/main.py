# возвращает кортеж от первого до второго вхождения element
def slicer(original_tuple, element):
    count = original_tuple.count(element)
    if count >= 2:
        index_1 = original_tuple.index(element)
        index_2 = original_tuple.index(element, index_1 + 1)
        return original_tuple[index_1:index_2+1]
    elif count == 1:
        index_1 = original_tuple.index(element)
        return original_tuple[index_1:]
    else:
        return tuple()


# секция тест
'''sequence_3 = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
sequence_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sequence_1 = (3, 4, 5, 6, 7, 8, 9, 10)
sequence_element = 2

print("Ответ в консоли:", slicer(sequence_1, sequence_element))'''

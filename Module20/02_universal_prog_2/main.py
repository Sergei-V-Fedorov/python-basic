from math import factorial

''' Теорема Вильсона. Натуральное число p > 1 является простым тогда и только тогда,
когда (p − 1)! + 1 делится на p '''
def is_prime(natural_number):
    return natural_number > 1 and \
           not (factorial(natural_number - 1) + 1) % natural_number


def select_elements_with_prime_indexes(original_sequence):
    return [element for index, element in enumerate(original_sequence) if is_prime(index)]


# секция тест
# первые простые числа 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
'''sequence_1 = range(50)
sequence_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Ответ в консоли:", select_elements_with_prime_indexes(sequence_1))'''

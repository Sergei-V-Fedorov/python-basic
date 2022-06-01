# формулировку задачи не понял
import math

factorial_dict = {}


def calculating_math_func(data, dictionary=factorial_dict):
    if data in factorial_dict:
        result = factorial_dict[data]
        print(f"Факториал числа {data} уже посчитан и равен {result}")
    else:
        print(f"Факториал числа {data} еще не вычислялся")
        result = math.factorial(data)
        factorial_dict[data] = result

    result /= data ** 3
    result = result ** 10
    return result


for number in (1, 2, 3, 3, 2, 1, 4, 5, 5):
    calculating_math_func(number)

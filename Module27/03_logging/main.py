from typing import Callable
from functools import wraps
import datetime as dt


def logging(func: Callable) -> Callable:

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            print("\nВызывается функция", func.__name__)
            print(func.__doc__)
            result = func(*args, **kwargs)
            return result
        except Exception as exception:
            with open("function_errors.log", 'a') as log_file:
                log_file.write("[{datetime}]: функция '{func}' вызвала ошибку {excep}\n".format(
                    datetime=dt.datetime.now(), func=func.__name__, excep=str(exception).upper()))

    return wrapped_func


@logging
def division(divisible: int, divisor: int) -> float:
    """Вычисляет отношение двух чисел"""
    return divisible / divisor


@logging
def is_capital(word: str) -> bool:
    """Определяет начинается ли слово с заглавной буквы"""
    return word[0].isupper()


test_1 = is_capital("Hello")
print(test_1)
test_2 = is_capital([1, 2, 3])
print(test_2)
test_3 = is_capital("hello")
print(test_3)
test_4 = is_capital(1)
print(test_4)
test_5 = division(1, 0)
print(test_5)
test_6 = division(3, 3)
print(test_6)
test_7 = division(7, 0)
print(test_7)

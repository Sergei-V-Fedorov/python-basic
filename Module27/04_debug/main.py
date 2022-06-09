from typing import Callable
from functools import wraps


def debug(func: Callable) -> Callable:
    """Декоратор, выводящий название функции, её аргументы и возвращаемый результат"""
    @wraps(func)
    def wrapped_func(*args, **kwargs):

        recieved_arguments = []
        for arg in args:
            recieved_arguments.append(repr(arg))

        for kwarg in kwargs:
            recieved_arguments.append(str(kwarg) + '=' + repr(kwargs[kwarg]))

        recieved_arguments = ', '.join(recieved_arguments)
        print("\nВызывается {name}({args})".format(name=func.__name__, args=recieved_arguments))

        result = func(*args, **kwargs)
        print(f"'{func.__name__}' вернула значение '{result}'")

        return result

    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"))
print(greeting("Женя", 45))
print(greeting("Миша", age=100))
print(greeting(name="Катя", age=16))

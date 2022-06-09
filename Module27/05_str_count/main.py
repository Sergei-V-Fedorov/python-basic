from typing import Callable
from functools import wraps


def counter(func: Callable) -> Callable:
    """Декоратор, подсчитывающий кол-во вызовов декорируемой функции"""

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        func(*args, **kwargs)
        print("Функция {func} вызвана {count} раз(а)".format(
            func=func.__name__, count=wrapped_func.count))
    wrapped_func.count = 0
    return wrapped_func


@counter
def hello() -> None:
    print("Hello, word!")


for _ in range(3):
    hello()

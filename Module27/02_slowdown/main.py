from functools import wraps
from typing import Callable
import time


def wait(func: Callable) -> Callable:
    """Декоратор, откладывающий выполнение ф-ии на 2 сек"""

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        print("Ждите")
        time.sleep(2)
        func(*args, **kwargs)

    return wrapped_func


@wait
def hello() -> None:
    print("Hello, word!")


hello()

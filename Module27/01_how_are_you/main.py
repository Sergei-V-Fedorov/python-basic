from typing import Callable
from functools import wraps


def how_are_you(func: Callable) -> Callable:
    """Декоратор шаловливого Вани"""
    @wraps(func)
    def wrapped_fanc(*args, **kwargs):
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        func(*args, **kwargs)

    return wrapped_fanc


@how_are_you
def is_odd(number: int) -> None:
    if number % 2:
        print(f"{number} is odd")
    else:
        print(f"{number} is even")


@how_are_you
def hello() -> None:
    print("Hello, word!")


hello()
print()
is_odd(3)

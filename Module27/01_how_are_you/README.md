## Задача 1. Как дела?
### Что нужно сделать
Ваня что-то совсем заскучал на работе и решил побаловаться с кодом проекта. Он написал надоедливый декоратор, который при вызове декорируемой функции спрашивает у пользователя «Как дела?», вне зависимости от ответа отвечает что-то вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после такой выходки его чуть не уволили с работы.

Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.

Пример кода:
```python
@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
```

Результат:
```
Как дела? Хорошо.
А у меня не очень! Ладно, держи свою функцию.
<Тут что-то происходит...>
```

### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.
- Во всех декораторах используется `functools.wraps`.
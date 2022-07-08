# 1. Задача на декоратор с кешированием результата.
# Напишите функцию-декоратор, которая сохранит (закэширует) значение декорируемой функции multiplier (Чистая функция).
# Если декорируемая функция будет вызвана повторно с теми же параметрами — декоратор должен вернуть сохранённый
# результат, не выполняя функцию.

import functools
import random


def cache(func):
    """Кэш предыдущих вызовов функций"""
    @functools.wraps(func)
    def wrapper(*args):
        if args not in wrapper.cache:
            wrapper.cache[args] = func(*args)
        else:
            print('Данные взяты из кэша!: ', end='')
        return wrapper.cache[args]
    wrapper.cache = dict()
    return wrapper


@cache
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    for _ in range(10):
        print(multiplier(random.randint(1, 10)))

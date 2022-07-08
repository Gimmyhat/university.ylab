# 2. Задача на декоратор с параметрами.
# Надо написать декоратор для повторного выполнения декорируемой функции через некоторое время. Использует
# наивный экспоненциальный рост времени повтора (factor) до граничного времени ожидания (border_sleep_time).

import time


def retry(call_count, start_sleep_time, factor, border_sleep_time):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            print(f'Количество запусков = {call_count}')
            for i in range(call_count):
                t = (start_sleep_time * 2 ** i) * factor
                t = (min(border_sleep_time, t))
                time.sleep(t)
                print(f'Запуск номер {i + 1}. Ожидание {t} секунд. '
                      f'Результат декорируемой функций =  {func(*args, **kwargs)}')
        return _wrapper
    return retry_decorator


@retry(3, 1, 2, 7)
def add(x, y):
    return x + y


if __name__ == '__main__':
    add(4, 7)

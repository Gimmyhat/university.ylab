# Задача №3.
# Написать метод zeros, который принимает на вход целое число (integer) и
# возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

def zeros(n):
    return n / 5 + zeros(n / 5) if n >= 5 else 0


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

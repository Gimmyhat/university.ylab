# Задача №3.
# Написать метод zeros, который принимает на вход целое число (integer) и
# возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

def zeros(n):
    pow_of_5 = 5
    zero = 0

    while n >= pow_of_5:
        zero += n // pow_of_5
        pow_of_5 *= 5

    return zero


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

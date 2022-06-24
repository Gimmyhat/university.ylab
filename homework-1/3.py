# Задача №3.
# Написать метод zeros, который принимает на вход целое число (integer) и
# возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

def zeros(n):
    return sum(int(n / 5 ** i) for i in range(1, 10) if int(n / 5 ** i) >= 1)


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

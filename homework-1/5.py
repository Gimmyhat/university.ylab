# Задача №5.
# Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
# предел (limit), после чего попробуйте сгенерировать по порядку все числа.
# Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

# Поиск простых множителей числа n
def primfacs(n, i=2):
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n // i
        i += 1
    if n > 1:
        primfac.append(n)
    return primfac


def count_find_num(primesL, limit):
    # your code here
    k, mx = 0, 0
    for i in range(limit + 1):
        if set(primesL) == set(primfacs(i)):
            k += 1
            mx = i
    return [k, mx] if k else []


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

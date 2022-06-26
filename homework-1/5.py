# Задача №5.
# Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
# предел (limit), после чего попробуйте сгенерировать по порядку все числа.
# Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

from itertools import *
from math import prod


def count_find_num(primesL, limit):
    if prod(primesL) > limit:
        return []
    res = {0: [primesL]}
    for i in count(1):
        res[i] = res.setdefault(i, [res[i - 1][y] + [x]
                                    for x in primesL
                                    for y in range(len(res[i - 1]))
                                    if prod(res[i - 1][y] + [x]) <= limit])
        if not res[i]:
            break
    k, mx = 0, 0
    for key, value in res.items():
        res[key] = list(set(tuple(sorted(sub)) for sub in value))
        k += len(res[key])
        if res[key]:
            mx = max(mx, max([prod(x) for x in res[key]]))
    return [k, mx] if mx else []


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


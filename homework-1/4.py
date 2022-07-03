# Задача №4.
# Написать метод bananas, который принимает на вход строку и
# возвращает количество слов «banana» в строке.
#
# (Используйте - для обозначения зачеркнутой буквы)

import itertools


def bananas(s):
    result = set()
    for comb in itertools.combinations(range(len(s)), len(s) - 6):
        word = list(s)
        for i in comb:
            word[i] = '-'
        candidate = ''.join(word)
        if candidate.replace('-', '') == 'banana':
            result.add(candidate)
    return result

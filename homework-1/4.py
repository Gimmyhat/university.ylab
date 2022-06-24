# Задача №4.
# Написать метод bananas, который принимает на вход строку и
# возвращает количество слов «banana» в строке.
#
# (Используйте - для обозначения зачеркнутой буквы)

from itertools import product


def bananas(s) -> set:
    result = set()
    # Your code here!
    word = 'banana'
    l = len(s) - len(word)
    # задаем вариации с прочерками в слове s
    variations = (x for x in product((' ', '-'), repeat=len(s)) if x.count('-') == l)
    for var in variations:
        # подставляем '-' в слово s
        str_temp = ''.join(ch2 if ch1 == ' ' else ch1 for ch1, ch2 in zip(var, s))
        # если после манипуляций можно прочитать слово banana - заносим в result
        if str_temp.replace('-', '') == word:
            result.add(str_temp)

    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

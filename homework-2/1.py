import itertools


def paths(chain):
    res = [i for i in itertools.permutations(itertools.permutations(chain, 2), len(chain))]
    res = [''.join(x[0] for x in i) for i in res]
    res = set([x + chain[0] for x in res if len(set(x)) == len(chain) and x[0] == chain[0]])
    return res


def f(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


if __name__ == '__main__':
    points = dict(a=(0, 2), b=(2, 5), c=(5, 2), d=(6, 6), e=(8, 3))
    min_path = 10 ** 10
    min_chain = ''
    for i in paths('abcde'):
        var_path = 0
        for x, y in zip(i, i[1:]):
            var_path += f(points[x], points[y])
        min_path, min_chain = (var_path, i) if var_path < min_path else (min_path, min_chain)

    print(points[min_chain[0]], end=' -> ')
    s = (f'{points[y]}[{f(points[x], points[y])}]' for x, y in zip(min_chain, min_chain[1:]))
    print(f"{' -> '.join(s)} = {min_path}")

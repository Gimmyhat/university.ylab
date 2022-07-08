# 1. Задача на циклический итератор.
# Надо написать класс CyclicIterator.
# Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range, Range2, и т. д.),
# и когда достигнет последнего элемента, начинать сначала.

class CyclicIterator:

    def __init__(self, items):
        self.index = -1
        self.items = items

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.items[self.index % len(self.items)]


cyclic_iterator = CyclicIterator(range(6))
for i in cyclic_iterator:
    print(i)

from itertools import product


def dots(str):
    lst = []
    for prod in product(("", "."), repeat=len(str) - 1):
        mixed = [char for tpl in zip(str, prod + ("",)) for char in tpl]
        new_word = "".join(mixed)
        lst.append(new_word)
    return lst


x = dots('abc')
print(x)

import random


def random_num_list(n):
    for i in range(n):
        rng = random.randint(1, 100)
        lst.append(rng)
    return lst


def only_odd(lst):
    odd = []
    for i in lst:
        if i % 2 == 1:
            odd.append(i)
    return odd


def square(lst):
    sqr = []
    for i in lst:
        i **= 2
        sqr.append(i)
    return sqr


def sublist(lst, start, stop):
    sub = lst.copy()
    del sub[0:start]
    del sub[stop:len(lst)]
    return sub


lst = []
print("Here is the list:", random_num_list(5))
print("Odds in it are:", only_odd(lst))
print("Let's square each number:", square(lst))
print("Only the three middle values:", sublist(lst, 1, 3))

import math
import os


def lstA():
    path = os.getcwd()
    path += "/dn222ng_assignment3/files/file_10k_integers_A.txt"
    with open(path, "r") as file:
        data = file.read()
        str = data.replace(',', '')
        lst = str.split()
        int_lst = [int(i) for i in lst]
    return int_lst


def lstB():
    path = os.getcwd()
    path += "/dn222ng_assignment3/files/file_10k_integers_B.txt"
    with open(path, "r") as file:
        data = file.read()
        str = data.replace(':', ' ')
        lst = str.split()
        int_lst = [int(i) for i in lst]
    return int_lst


def mean(lst):
    res = round(sum(lst) / len(lst), 1)
    return res


def std(lst):
    avg = sum(lst) / len(lst)
    new_lst = []
    for i in lst:
        res = (i - avg) ** 2
        new_lst.append(res)
    new_mean = sum(new_lst) / len(new_lst)
    std = round(math.sqrt(new_mean), 1)
    return std


valuesA = lstA()
valuesB = lstB()
print("\nResult for file A:")
print(f'mean = {mean(valuesA)}, standard deviation = {std(valuesA)}')
print("\nResult for file B:")
print(f'mean = {mean(valuesB)}, standard deviation = {std(valuesB)}')

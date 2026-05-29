import random

lst = []
for i in range(100):
    rnd = random.randint(1, 10000)
    lst.append(rnd)

avg = round((sum(lst) / len(lst)), 2)
print(f'Largest value in list: {max(lst)}')
print(f'Smallest value in list: {min(lst)}')
print(f'Average value in list: {avg}')
lst.remove(max(lst))
print(f'Second largest value in list: {max(lst)}')

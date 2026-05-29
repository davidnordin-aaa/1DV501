import math


def distance(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    dist = round(dist, 3)
    return dist


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

print(f'\nThe distance between ({float(x1)},{float(y1)})', end="")
print(f' and ({float(x2)},{float(y2)}) is {distance(x1, y1, x2, y2)}')

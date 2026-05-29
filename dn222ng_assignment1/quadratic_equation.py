import math

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

res = (B**2) - (4*A*C)

if A == 0 or A and B == 0:
    print("There is only one solution then, namely", - C/B)
elif res < 0:
    print("There are no solutions")
else:
    s1 = (-B + math.sqrt(res)) / (2*A)
    s2 = (-B - math.sqrt(res)) / (2*A)
    if res == 0:
        print("There is one solution, namely", s1)
    elif res > 0:
        print("There are two solutions, namely", s1,"and", s2)
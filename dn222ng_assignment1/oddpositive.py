import random

num = random.randint(-10,10)

if num >= 1 and num % 2 == 0:
    print(num,"is positive and even")
elif num >= 1 and num % 2 == 1:
    print(num, "is positive and odd")
elif num <= -1 and num % 2 == 0:
    print(num, "is negative and even")
elif num <= -1 and num % 2 == 1:
    print(num,"is negative and odd")
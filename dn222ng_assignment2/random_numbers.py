import random

n = int(input("Enter number of integers to be generated: "))

if n < 0:
    print("Please enter a positive integer")
else:
    avg = 0
    maxi = 0
    mini = 101

    print("\nGenerated values: ", end="")
    for i in range(n):
        r = random.randint(1, 100)
        avg += r
        if maxi < r:
            maxi = r
        if mini > r:
            mini = r
        print(r, end=" ")

    average = str(round(avg / n, 2))
    mini = str(mini)
    maxi = str(maxi)
    print("\nAverage, min and max are", end=" ")
    print(average + ", " + mini + " and " + maxi)

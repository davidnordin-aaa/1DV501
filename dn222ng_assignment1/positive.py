integer = int(input("Please provide an integer: "))

if integer >= 1:
    print(integer,"is positive")
elif integer <= -1:
    print(integer, "is negative")
elif integer == 0:
    print(integer,"is zero")
else:
    print("Wrong input")
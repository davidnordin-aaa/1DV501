import random


def print_rolls(rolls):
    count = 0
    ones, twos, threes, fours, fives, sixs = 0, 0, 0, 0, 0, 0
    while count < rolls:
        r = random.randint(1, 6)

        if r == 1:
            ones += 1
        elif r == 2:
            twos += 1
        elif r == 3:
            threes += 1
        elif r == 4:
            fours += 1
        elif r == 5:
            fives += 1
        elif r == 6:
            sixs += 1
        count += 1

    most = max(ones, twos, threes, fours, fives, sixs)
    least = min(ones, twos, threes, fours, fives, sixs)

    diff = most - least
    res = diff / most
    print("For", rolls, "rolls, the difference is", round((res * 100), 2), "%")


counter = 0
throws = 10
while counter < 20:
    print_rolls(throws)
    throws *= 2
    counter += 1

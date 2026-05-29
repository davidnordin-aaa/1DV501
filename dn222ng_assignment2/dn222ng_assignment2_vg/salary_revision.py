def median(s):  # funktion för median
    s.sort()  # sorterar löner i storleksordning
    list = len(s)  # längd av listan
    med = (list-1) // 2  # mitten av listan
    if list % 2 == 0:  # ifall listan är jämn
        res = (int(s[med]) + int(s[med + 1])) / 2
        return int(res)  # returnar genomsnitt för de två mittersta värdena
    else:  # ifall listan är ojämn
        return s[med]  # returnar median för ojämna listor


def average(s):  # funktion för genomsnitt
    s = [int(i) for i in s]  # konverterar listans värden från string till int
    return round(sum(s) / len(s))  # räknar ut genomsnitt och returnar


def gap(s):  # funktion för gap
    s.sort()  # sorterar lista i storleksordning
    s = [int(i) for i in s]  # samma som på rad 13
    mx = max(s)  # max värde i listan
    mn = min(s)  # min värde i listan
    return round(mx - mn)  # returnerar max - min som blir gap


s = input("Provide salaries: ")  # input för löner som 321 213 2314
sal = s.split()  # delar upp alla s värden i en lista

print(f'Median: {median(sal)}')  # output för median
print(f'Average: {average(sal)}')  # output för average
print(f'Gap: {gap(sal)}')  # output för gap

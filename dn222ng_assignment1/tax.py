salary = int(input("Please provide monthly income: "))
tax1, tax2, tax3 = salary, salary, salary

if 0 < salary < 38000:
    tax1 *= 0.3
    print("Corresponding tax income:",round(tax1))
elif 38000 < salary < 50000:
    tax1 *= 0.3
    tax2 -= 38000
    tax2 *= 0.05
    print("Corresponding income tax:",round(tax1 + tax2))
elif salary > 50000:
    tax1 *= 0.3
    tax2 -= 38000
    tax2 *= 0.05
    tax3 -= 50000
    tax3 *= 0.05
    print("Corresponding income tax:",round(tax1 + tax2 + tax3))
else:
    print("Wrong input:", salary)
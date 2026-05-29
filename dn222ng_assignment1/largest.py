print("Please provide three integers A, B, C.")
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A > B and A > C:
    print("The largest number is:", A)
elif B > A and B > C:
    print("The largest number is:", B)
elif C > A and C > B:
    print("The largest number is:", C)
else:
    print("Wrong input")
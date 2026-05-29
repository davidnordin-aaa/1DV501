n = int(input("Enter a positive integer: "))
i = 0
k = 0

if n < 0:
    print("Please enter a positive integer!")
else:
    while i < n:
        k += 2
        i += k

k -= 2
print(k, "is the largest k such that 0+2+4+6+...+k <", n)

s = int(input("Initial savings: "))
p = int(input("Interest rate (in percentages): "))
y = int(input("Number of years: "))

res = round(s*((p/100)+1)**y)

print("The value of your savings after " + str(y) +" years is: " + str(res))
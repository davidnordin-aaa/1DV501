num = int(input("Provide a three digit number: "))

num1 = num % 10
num2 = (num//10) % 10
num3 = (num // 10) // 10
res = num1 + num2 + num3

print(res)
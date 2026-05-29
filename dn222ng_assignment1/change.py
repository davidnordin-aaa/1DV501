price = float(input("Price: "))
pay = float(input("Payment: "))

change = pay - price
change = round(change)
print("\nChange: " + str(change) + " kr")

if change >= 1000:
    change -= 1000
    print("1000kr bills: 1")
else:
    print("1000kr bills: 0")
if change >= 500:
    change -= 500
    print("500kr bills: 1")
else:
    print("500kr bills: 0")
if change >= 200:
    change -= 200
    print("200kr bills: 1")
else:
    print("200kr bills: 0")
if change >= 100:
    change -= 100
    print("100kr bills: 1")
else:
    print("100kr bills: 0")
if change >= 50:
    change -= 50
    print("50kr bills: 1")
else:
    print("50kr bills: 0")
if change >= 20:
    change -= 20
    print("20kr bills: 1")
else:
    print("20kr bills: 0")
if change >= 10:
    change -= 10
    print("10kr coins: 1")
else:
    print("10kr coins: 0")
if change >= 5:
    change -= 5
    print("5kr coins: 1")
else:
    print("5kr coins: 0")
if change >= 2:
    change -= 2
    print("2kr coins: 1")
else:
    print("2kr coins: 0")
if change >= 1:
    change -= 1
    print("1kr coins: 1")
else:
    print("1kr coins: 0")
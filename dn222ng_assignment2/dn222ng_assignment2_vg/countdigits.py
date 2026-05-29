n = int(input("Enter a large positive integer: "))  # input
if n < 0:
    print("Please enter a positive integer")  # n ska vara positiv
else:
    nu = str(n)  # ändrar n till en string
    odd, zero, even = 0, 0, 0
    count = 1

    for y in nu:
        y = nu[len(nu) - count]  # y = siffran längst bak i str
        if y in "13579":
            odd += 1  # ifall y är ojämn blir odd += 1
        elif y in "2468":
            even += 1  # samma princip som på rad 12 fast för jämnt
        elif y in "0":
            zero += 1  # samma princip som på rad 12 fast för nollor
        count += 1  # count påverkar y i nästa iteration, kollar siffran före n

    print(f'Zeros: {zero}\nOdd: {odd}\nEven: {even}')  # output på tre rader

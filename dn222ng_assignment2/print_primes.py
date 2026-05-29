num = int(input("How many primes? "))
count = 0
n = 2

while count < num:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
        print(n, end=" ")
        if count % 10 == 0:
            print()
    n += 1

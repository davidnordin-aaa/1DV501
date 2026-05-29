import random


def is_palindrome(s):
    sy = ''.join(i for i in s if i.isalpha())
    sx = sy.casefold()
    res = sx[::-1]
    if sx == res:
        return True
    elif sx != res:
        return False


li = ["A nut for a jar of tuna.", "Madam", "Ni talar bra latin!"]
ex = random.choice(li)
print(f'Some examples of palidromes: "Was it a rat I saw?" or "{ex}"')

string = input("Please enter a string that is a palindrome: ")
print(is_palindrome(string))

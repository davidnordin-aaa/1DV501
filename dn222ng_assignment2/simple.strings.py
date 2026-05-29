def first_last(s):
    first = s[0]
    last = s[len(s) - 1]
    return first, last


def char_types(s):
    vowels, consonants = 0, 0
    for i in s:
        if i in "AaEeIiOoUu":
            vowels += 1
        elif i in "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz":
            consonants += 1
    return vowels, consonants


def char_symbol_number(s):
    letters = 0
    symbols = 0
    numbers = 0
    for i in s:
        if i in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
            letters += 1
        elif i in ".,! ":
            symbols += 1
        elif i in "1234567890":
            numbers += 1
    return letters, symbols, numbers


string = input(str("Enter a string: "))

vow, con = char_types(string)
first, last = first_last(string)
let, sym, num = char_symbol_number(string)

print(f'First and last in "{string}": {first} {last}')
print(f'In that sentence, the number of vowels is {vow}', end="")
print(f' and the number of consonants is {con}')
print(f'In the sentence "{string}" the number of letters is {let},', end="")
print(f' symbols is {sym} and numbers is {num}')

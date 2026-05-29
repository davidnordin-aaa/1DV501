import random

hearts1 = ["Ace of Hearts", "2 of Hearts", "3 of Hearts"]
hearts2 = ["4 of Hearts", "5 of Hearts", "6 of Hearts"]
hearts3 = ["7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts"]
hearts4 = ["Knight of Hearts", "Queen of Hearts", "King of Hearts"]
hearts = hearts1 + hearts2 + hearts3 + hearts4

dia1 = ["Ace of Diamonds", "2 of Diamonds", "3 of Diamonds"]
dia2 = ["4 of Diamonds", "5 of Diamonds", "6 of Diamonds"]
dia3 = ["7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds"]
dia4 = ["Knight of Diamonds", "Queen of Diamonds", "King of Diamonds"]
dia = dia1 + dia2 + dia3 + dia4

spa1 = ["Ace of Spaces", "2 of Spaces", "3 of Spacees"]
spa2 = ["4 of Spaces", "5 of Spaces", "6 of Spaces"]
spa3 = ["7 of Spaces", "8 of Spaces", "9 of Spaces", "10 of Spaces"]
spa4 = ["Knight of Spaces", "Queen of Spaces", "King of Spaces"]
spa = spa1 + spa2 + spa3 + spa4

clu1 = ["Ace of Clubs", "2 of Clubs", "3 of Clubs"]
clu2 = ["4 of Clubs", "5 of Clubs", "6 of Clubs"]
clu3 = ["7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs"]
clu4 = ["Knight of Clubs", "Queen of Clubs", "King of Clubs"]
clu = clu1 + clu2 + clu3 + clu4

deck = hearts + dia + spa + clu
print("My hand:")
for i in range(5):
    rng = random.choice(deck)
    print(rng)

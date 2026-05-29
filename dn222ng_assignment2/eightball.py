import random

respons1 = ["Ask again later", "As i see it, yes", "Concentrate and ask again"]
respons2 = ["Very doubtful", "Better not tell you now"]
lst = respons1 + respons2

question = input("Ask the magic 8-ball your question: ")

if question == "stop":
    exit()
while question != "stop":
    res = random.choice(lst)
    print(f'The magic 8-ball says: {res}')
    question = input("Ask the magic 8-ball your question: ")

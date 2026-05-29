import random


def pronoun(rnd):
    pronouns = "I", "They", "You", "It", "We"
    rnd = random.choice(pronouns)
    print(rnd, end=" ")


def verb(rnd):
    verbs = "will eat", "will see", "will pull", "will touch", "will lift"
    rnd = random.choice(verbs)
    print(rnd, end=" ")


def noun(rnd):
    nouns = "a house", "a car", "a computer", "a tree", "a bike"
    rnd = random.choice(nouns)
    print(rnd, end=" ")


iteration = 10
for i in range(iteration):
    pronoun(iteration)
    verb(iteration)
    noun(iteration)
    print()

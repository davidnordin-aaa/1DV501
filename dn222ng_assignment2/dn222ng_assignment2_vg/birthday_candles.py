box, boxbox, age, candles = 0, 0, 0, 0

for i in range(100):  # iteration 100 gånger
    age += 1  # öka ålder med 1 varje iteration
    box = 0  # nollställer köpta box varje iteration
    while candles < age:  # när candles är mindre än ålder
        box += 1  # köper 1 box i varje iteration
        boxbox += 1  # boxbox = totala box
        candles += 24  # köper 24 candles i varje iteration
    candles -= age  # suptraherar candles med age
    if box > 0:  # printar meningen bara ifall lådor köptes
        print(f'Before birthday {age}, buy {box} box(es)')

print(f'Total number of boxes: {boxbox}, Remaining candles: {candles}')

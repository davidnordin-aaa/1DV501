import os


def get_words(path, name):
    path += name
    with open(path, "r", encoding='utf-8') as file:
        count = 0
        data = file.read()
        words = set(data.split())
        for word in words:
            count += 1
        words2 = data.split()
        dct = {}
        for word in words2:
            if len(word) > 4:
                if word in dct:
                    dct[word] = dct[word] + 1
                else:
                    dct[word] = 1
        value_sorted = sorted(dct.items(), key=lambda tpl: tpl[1])
        value_sorted.reverse()
        for i in range(10):
            print(value_sorted[i][0], ":", value_sorted[i][1])
        print()
        return count


path = os.getcwd()
brian = '\\files\\brian.txt'
news = '\\files\\swenews.txt'

print(f'Number of unique words in Life of Brian: {get_words(path, brian)}')
print()
print(f'Number of unique words in Swedish News: {get_words(path, news)}')

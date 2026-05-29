import os


def get_words(path, file_name):
    path += file_name
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        non = [':', '.', '[', ']', '!', ',', '?', '&', '"', '-', '*']
        word = ['•', '▪', '”', '½', '–', '(', ')', '/', '%']
        nonwords = non + nums + word
        for i in nonwords:
            if i in data:
                data = data.replace(i, '')
        res = data.split()
    return res


def save_words(path, output_file, words):
    path += output_file
    with open(path, "w", encoding='utf-8') as file:
        for i in words:
            file.write(i)
            file.write("\n")


path = os.getcwd()
input_file = '\\files\\swe_news.txt'

words = get_words(path, input_file)

output_file = f'/files/swenews_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved,', len(words), 'words in the file', path + output_file)

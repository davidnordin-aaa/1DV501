import os


def get_words(path, file_name):
    path += file_name
    with open(path, "r") as file:
        data = file.read()
        nonwords = [':', '.', '[', ']', '!', ',', '?', '&', '"', '-', '*']
        for i in nonwords:
            if i in data:
                data = data.replace(i, '')
        res = data.split()
    return res


def save_words(path, output_file, words):
    path += output_file
    with open(path, "w") as file:
        for i in words:
            file.write(i)
            file.write("\n")


path = os.getcwd()
input_file = '\\files\\life_of_brian.txt'

words = get_words(path, input_file)

output_file = f'/files/brian_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved,', len(words), 'words in the file', path + output_file)

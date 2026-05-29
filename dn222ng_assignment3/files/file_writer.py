import os


def writing(path, name, content):
    path + f'\\files\\{name}'
    with open(path, "w") as file:
        file.write(content)


path = os.getcwd
name = str(input("Name of the file: "))
print('Enter the content and end with "stop":')

content = str("")
inp = str(input("> "))
while inp != "stop":
    content += inp
    content += "\n"
    inp = str(input("> "))
print("Writing to file....")

writing(path, name, content)

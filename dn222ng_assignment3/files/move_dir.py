import os


def alt():
    print("\n1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit\n")


def list_dir(dir_path):
    values = []
    for entry in dir_path:
        if entry.is_dir():
            values.append(entry.name)
    return '\n'.join(values)


def list_files(dir_path):
    values = []
    for entry in dir_path:
        if entry.is_file():
            values.append(entry.name)
    return "\n".join(values)


def change_dir():
    change = str(input("Name of directory to enter: "))
    os.chdir(change)


alt()
inp = int(input("==>"))

while inp != 4:
    path = os.getcwd()
    entries = os.scandir(path)
    if inp == 1:
        print(list_dir(entries))
    elif inp == 2:
        change_dir()
    elif inp == 3:
        print(list_files(entries))
    alt()
    inp = int(input("==> "))
print("Exiting")

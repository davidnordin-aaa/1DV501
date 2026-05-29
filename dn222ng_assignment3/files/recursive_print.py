import os


def print_sub(dir_path):
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
            print_sub(entry.path)


path = "/Users/david/software/python_courses/1DV501"
print_sub(path)

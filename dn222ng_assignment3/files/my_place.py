import os


def count_directories(dir_path):
    no_dir = 0
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            no_dir += 1
    return no_dir


def count_files(dir_path):
    no_files = 0
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_file():
            no_files += 1
    return no_files


path = os.getcwd()
print(f"I am right now at {path}")
n_dirs = count_directories(path)
print(f'Below me I have {n_dirs} directories/folder')
n_files = count_files(path)
print(f'This directory contains {n_files} files')

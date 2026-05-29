def reading(path, name):
    path += f'/dn222ng_assignment3/files/{name}'
    with open(path, "r") as file:
        lines = 0
        for line in file:
            lines += 1
        print(f'Lines in file: {lines}')
    with open(path, "r") as file:
        print("Content of file: ")
        for line in file:
            print(line.strip())


name = str(input("What is the name of the file to read? "))
path = "/Users/david/software/python_courses/1DV501/"
reading(path, name)

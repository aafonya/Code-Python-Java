# Write a function that open a file for reading and returns the number of
# bytes and newlines('\n').


def readFile(filename):
    f = open(filename)
    size = 0
    lines = 0

    buf = f.read()
    while buf != "":
        buf = f.read(1)
        size += 1
        if buf == '\n':
            lines += 1

    f.close()                # close file

    return (size, lines)

print(readFile('import_inventory.csv'))

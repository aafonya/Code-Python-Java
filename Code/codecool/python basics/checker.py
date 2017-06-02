
def inputread(inputstring):
    while True:
        checker = input(inputstring)
        try:
            checker = int(checker)
            if checker < 0 or checker > 10:
                continue
            else:
                return checker
        except ValueError:
            if checker == "exit":
                quit()


inputread("adj be egy számot")


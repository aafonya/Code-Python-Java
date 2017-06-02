# Create a function that appends the name and email to the end of a named file.
def addEmail(filename, name, email):
    f = open(filename, 'a')  # replace the mode

    # Append name and email, each record should end with '\n'.
    f.write(name + '\n' + email + '\n')

    # close file
    f.close()

    return f  # do not remove this line

addEmail("py_tut.txt", "J", "suholy@gmail.com")
addEmail("py_tut.txt", "K", "zsolna@gmail.com")

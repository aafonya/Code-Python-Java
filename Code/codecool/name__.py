def main():
    # __name__ is a special variable - python sets these before reading any
    # code
    print("First Module's name: {}".format(__name__))

    # if we import a module - __name__ will be set to the name of these of the
    # imported module
    import name__sec
    print("Second Module's name: {}".format(__name__))

if __name__ == '__main__':
    main()

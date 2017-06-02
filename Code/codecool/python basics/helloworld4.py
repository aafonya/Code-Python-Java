def Hello(name=" world!"):
    """Welcomes the user"""
    print("Hello " + name + "!")

username = input("What is your name?")

if len(username) > 1:
    Hello(username)
else:
    Hello()
 
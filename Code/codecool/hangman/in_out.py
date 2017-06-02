# Already implemented, no need to change this
# This functions prints the various parts of the hanger (no idea how the parts are called)
# Everytime a wrong answer is given, it prints more parts of the hanger
# The function should recieve an int number : the incorrect answers
# counted so far


def print_hanger(number_of_incorrect):
    list_of_items = [["Hangman Game"],
                     ["+----------"],
                     ["|\n+----------"],
                     ["|\n|\n+----------"],
                     ["|\n|\n|\n+----------"],
                     ["|\n|\n|\n|\n+----------"],
                     ["|\n|\n|\n|\n|\n+----------"],
                     ["+-------+\n|\n|\n|\n|\n|\n+----------"],
                     ["+-------+\n|       |\n|       O\n|      -+-\n|       ^\n|\n+----------"]]
    if number_of_incorrect >= 8:
        print(list_of_items[8][0] + "\nGame Over!")
    else:
        print(list_of_items[number_of_incorrect][0])

# First, prints only underlines (the correct amount) ,
# and when the input is a correct letter,changes underline to the given char at the right place
#
# examples:  -at start: _ _ _ _ _ _
# When input "b" is a correct char in the word:    _ _ _ b _ _
# If the game is over, this shouldn't print anything
# letter_list : list


def print_words(letter_list):

    pass


# imports words from file and returns a dictionary where the key is the length of the words
# and the value is a list containing the words
# return : dictionary


def file_import(filename):
    words_from_file = open(filename).readlines()
    len_words = {}

    for line in words_from_file:
        len_words[line[0]] = []
        for words in words_from_file[[line]]:
            append.len_words[line[0]](words)

    words_from_file.close()
    # input from the user, it can only be a string word,
    # or a letter(should handle lower and uppercase letters as well).
    # return : string


def user_input():
    pass

# The starting menu, it should print the 3 difficulties,
# and a help/exit option
# returns an int number : difficulty


def print_menu():
    pass

# Prints out a message to the user
# msg : string


def print_msg(msg):
    pass

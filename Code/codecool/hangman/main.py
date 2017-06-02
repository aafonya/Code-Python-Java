import in_out
import time
import action


# Calling functions from in_out and 'action' should happen here
# The game is done, when the user enters the correct word,
# or completes the correct word using only one letter at a time.
# There should be 3 different diffuculity, easy - 6 letter word,
# medium - 8 letter word, or hard - 10 letter word
# If the game is won/lost it should ask the player if he/she wants to try again
def main():
    in_out.file_import("words.txt")


if __name__ == "__main__":
    main()

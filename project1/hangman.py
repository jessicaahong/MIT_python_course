"""Fri May 13 2016"""

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
import string
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = get_word() 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    is_won = True
    for letter in secret_word:
        if letter not in letters_guessed:
            is_won = False
    return is_won
    # pass # This tells your code to skip this function; delete it when you
    #      # start working on this function


def print_guessed():
    '''
    Returns a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    global secret_word
    global letters_guessed
    
    # create list to hold characters that were guessed
    built_word = []
    # create list of all characters
    remaining_letters = list(string.ascii_lowercase)
    # loop through each letter in string secret_word
    for letter in secret_word:
        # if that letter has been guessed, add that letter to built_word
        if letter in letters_guessed:
            built_word.append(letter)
        # if letter hasn't been guessed, add placeholder '-' to built_word
        else:
            built_word.append('-')
    # for each letter that has already been guessed, remove letter from remaining_letters
    for letter in letters_guessed:
        remaining_letters.remove(letter)

    # transform built_word and remaining_letters to strings and create instructional message
    output = "The word is %s.\nLetters you haven't guessed: %s" % (join(built_word,''), join(remaining_letters,'|'))
    # return instructional message
    return output

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    print "Let's play hangman!"
    while mistakes_made < MAX_GUESSES:
        print_hangman_image(mistakes_made)
        print
        print print_guessed()
        print "You have", MAX_GUESSES - mistakes_made, "guesses left!"

        # Get user input
        guess = raw_input("Choose a letter, or the word 'guess' to try to guess the full word: ")
        # If the player wants to guess the word...
        if guess.lower() == 'guess':
            # Get the guessed word input
            guessed_word = raw_input("Guess the word: ")
            # If the word is not a string of letters, print error message
            if guessed_word.isalpha() != True:
                print "Invalid input"
            # Else if the word is guessed correctly, have player win
            elif guessed_word.lower() == secret_word:
                print "You guessed the word correctly! The word is:", secret_word
                print "You Win!"
                break
            # And if the word is guessed incorrectly, detract two guesses
            else:
                print "You have guessed the word incorrectly. You lose two guesses."
                mistakes_made += 2
        else:
            # Print error if guess is not a single letter
            if (guess.isalpha() != True) or (len(guess) != 1):
                print "Invalid input."
            # Print error if guess has already been guessed
            elif guess.lower() in letters_guessed:
                print "You've already guessed that letter! Try again."
            # If guess has not already been guessed...
            elif guess.lower() not in letters_guessed:
                # Add guessed letter to letters_guessed
                letters_guessed.append(guess.lower())
                # See if guessed letter is in secret_word
                if guess.lower() in secret_word:
                    print guess, "is in the word!"
                    # If the player has won, print success message and end game
                    if word_guessed():
                        print "Correct! The word was:", secret_word
                        print "You win!"
                        break
                # Else if the guessed letter is not in secret_word
                else:
                    print guess, "is not in the word!"
                    mistakes_made += 1
    # Check to see if player has lost. If the player has made the maximum allowed mistakes, they lose.
    if mistakes_made == MAX_GUESSES:
        print_hangman_image(mistakes_made)
        print "You've run out of guesses. You lose!"
        print "The word was:", secret_word
    return None

play_hangman()


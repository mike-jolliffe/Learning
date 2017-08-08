# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #split the secretWord string into a list of letters
    secretWord_list = list(secretWord)

    #for each letter in the the secretWord list
    for letter in secretWord_list:

        #check if the letter hasn't been guessed
        if not letter in lettersGuessed:
            return False

    #if all the letters have been guessed, return True for isWordGuessed()
    return True

#isWordGuessed('apple', ['a', 'b', 'e', 'p', 'l'])

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #split the secretWord string into a list of letters
    secretWord_list = list(secretWord)

    #instantiate the string that will show user the word with correct letters
    word = ""

    for letter in secretWord_list:
        if letter in lettersGuessed:
            word += (letter + " ")
        else:
            word += '_ '

    return word

#getGuessedWord('apple', ['a', 'b', 'l'])

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #create a list of all available lowercase letters
    available = list(string.ascii_lowercase)

    #remove guessed letters from available letters list
    for letter in lettersGuessed:
        if letter in available:
            available.remove(letter)

    #convert available letters list to a string
    available = ''.join(available)
    return available


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #instantiate the hangman game
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    print('-----------------------')
    #establish the number of guesses and an empty list to grab letters guessed
    num_guesses = 8
    guessed = []

    while num_guesses > 0:

        #print number of guesses
        print ('You have {} guesses left.'.format(num_guesses))

        #grab and print letters available for guessing
        available = getAvailableLetters(guessed)
        print ('Available Letters: {}'.format(available))

        #grab user guess
        guess = raw_input('Please guess a letter: ')

        #check guess to make sure it's an available letter
        if guess in available:
            guessed.append(guess.lower())

        else:
            print ('Oops! You\'ve already guessed that letter: {}'.format(getGuessedWord(secretWord, guessed)))
            print ('-----------------------------')
            continue
            
        #check if letter is in the secretWord
        if guess in list(secretWord):
            print ('Good guess: {}'.format(getGuessedWord(secretWord, guessed)))
            print ('-----------------------------')
            #if it is, check for win
            if isWordGuessed(secretWord, guessed) == True:
                print ("Congratulations, you won!")
                break

        else:
            #if letter isn't in secretWord decrement number of guesses
            print ('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, guessed)))
            num_guesses -= 1

    #if run out of number of guesses
    print ('Sorry you ran out of guesses! The word was {}'.format(secretWord))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

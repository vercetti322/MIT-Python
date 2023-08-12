# The purpose of this file is to test the individual functions to validate the coding process
WORDLIST_FILENAME = "Problem Sets\\pset_2\\ps2\\words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file (for accessing the file)
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string (for reading line by line)
    line = inFile.readline()
    # wordlist: list of strings (for splitting each line into multiple words)
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


import string
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char not in letters_guessed:
            return False
    
    return True

# if (is_word_guessed('appllee', letters_guessed={'a','p','l','e'})):
#     print("True")
    
# else:
#     print("False")

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        
        else:
            guessed_word += " _ "
            
    return guessed_word

# print(get_guessed_word('apple', letters_guessed={'p'}))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Use directly as a function call without embedding in print statement
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            print(char, end='')
    print()
            
# get_available_letters(letters_guessed={'e'})

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Welcome Message
    print("Welcome to the game Hangman! ")
    print("I am thinking of a word that is", len(secret_word), "letters long. ")
    
    # Initialize variables
    guesses = 6
    letters_guessed = []
    warnings = 3
    
    # Loop code
    while guesses > 0:
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You guessed the word.")
            break
        
        print("You have", guesses, "guesses left.")
        get_available_letters(letters_guessed)
        letter = input("Please guess a letter: ")
        
        # Logical steps
        while not str.isalpha(letter):
            if warnings >= 1:
                print("Oops! That is not a valid letter. You have", (--warnings), "warnings left")
                letter = input("Please guess a letter: ")
            else:
                --guesses
        
        if str.lower(letter) in letters_guessed:
            if warnings >= 1:
                print("Oops! You have already guessed that word. You have", (--warnings), "warnings left")
                letter = input("Please guess a letter: ")
            else:
                --guesses
                
        if str.lower(letter) not in secret_word:
            if str.lower(letter) in {'a', 'e', 'i', 'o', 'u'}:
                guesses -= 2
            else:
                guesses -= 1
        
        letters_guessed.append(str.lower(letter))
        if str.lower(letter) not in secret_word:
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        else :
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            
        print("______________________________________________________")
        
    # Concluding lines (if-any)
    if guesses == 0:
        print("Sorry, you ran out of guesses. The word was:", secret_word)
        
# hangman('apple')

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
      return False
    else:
      for i in range(len(my_word)):
          if my_word[i] != '_':
            if my_word[i] != other_word[i]:
                return False
    return True
  
# if(match_with_gaps('ai _ l _', 'apple')):
#     print("Yes")
# else:
#     print("No")

wordlist = load_words()
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for string in wordlist:
        if match_with_gaps(my_word, string):
            print(string, end=' ')
    print()
    
# show_possible_matches('a _ _ l')

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Welcome Message
    print("Welcome to the game Hangman! ")
    print("I am thinking of a word that is", len(secret_word), "letters long. ")
    
    # Initialize variables
    guesses = 6
    letters_guessed = []
    warnings = 3
    print("You have", warnings, "warnings left.")
    print("______________________________________________________")
    
    # Loop code
    while guesses > 0:
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You guessed the word.")
            score = guesses * len(letters_guessed)
            print("Your total score for this game is:", score)
            break

        print("You have", guesses, "guesses left.")
        print("Available letters: ", end='')
        get_available_letters(letters_guessed)
        letter = input("Please guess a letter: ")

        if letter == '*':
            my_word = get_guessed_word(secret_word, letters_guessed)
            print("Available words: ")
            show_possible_matches(my_word)

        # Logical steps
        else:
            while not str.isalpha(letter):
                if warnings >= 1:
                    warnings -= 1
                    print("Oops! That is not a valid letter. You have", warnings, "warnings left")
                    letter = input("Please guess a letter: ")
                else:
                    guesses -= 1

            if str.lower(letter) in letters_guessed:
                if warnings >= 1:
                    warnings -= 1
                    print("Oops! You have already guessed that word. You have", warnings, "warnings left")
                    letter = input("Please guess a letter: ")
                else:
                    guesses -= 1

            if str.lower(letter) not in secret_word:
                if str.lower(letter) in {'a', 'e', 'i', 'o', 'u'}:
                    guesses -= 2
                else:
                    guesses -= 1

            letters_guessed.append(str.lower(letter))
            if str.lower(letter) not in secret_word:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))

            print("______________________________________________________")
            
    # Concluding lines (if-any)
    if guesses == 0:
        print("Sorry, you ran out of guesses. The word was:", secret_word)

# hangman_with_hints("apple")
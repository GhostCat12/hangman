import random

word_list = ['cherry' , 'watermelon' , 'mango' , 'strawberry' , 'banana' ]


class Hangman:
    '''
    This class represents the game Hangman

    Attributes: 
        word: (str) - The word to be guessed, picked randomly from the word_list.
        word_guessed: (list) - A list of the letters of the word, with _ for each letter not yet guessed.
        num_letters: (int) - The number of unique letters in the word that have not been guessed yet.
        num_lives: (int) - The number of lives the player has at the start of the game.
        word_list: (list) - Word bank for the computer to choose from
        list_of_guesses: (list) - A list of the guesses that have already been tried. Initialised as empty. 

    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word)) #needs fix
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list()
    
    
    def check_guess(self, guess):
        '''
        This function is used to check the guessed letter is in the word to be guessed.

        If guessed letter is inside the word, the guessed letter replaces the underscore 
        placeholder inside word_guessed list. 
        e.g. ['_', '_', '_', '_', '_'] -> ['a', '_', '_', '_', '_']
        If guessed incorrectly, num_lives decrease by 1.   
    
        Args: 
        guess (str): letter guessed by user.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.word_guessed[self.word.index(guess)] = guess
            self.num_letters -= 1        
        else: 
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left") 


    def ask_for_input(self):
        ''' 
        This function is used to ask for the user to input a guessed letter and runs checks. 
        
        If the guess input is not a single alphabetical character and has been previously guessed,
        the user is told to input again.
        Otherwise the check_guess method is called, and guess is appended to the list_of_guesses list. 
        '''
        while True:
            guess = input('Guess a single alphabetical letter : ')
            if (len(guess) != 1) or (guess.isalpha() == False) :
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            
test = Hangman(word_list) 
test.ask_for_input()          

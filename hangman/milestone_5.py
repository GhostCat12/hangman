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
        self.word = random.choice(word_list)   # randomly choose word from word_list
        self.word_guessed = ['_'] * len(self.word) # create a list of '_' that is length of chosen word
        self.num_letters = len(set(self.word)) # number of unique letters in chosen word
        self.num_lives = num_lives # number of lives - can set game dificulty
        self.word_list = word_list # list acting as a word bank for computer to choose from
        self.list_of_guesses = list() # empty list, will hold guesses made by user.
        print(f"{'-'*60} \n H A N G M A N \n \n number of lives: {self.num_lives} \n \n The mystery word has {self.num_letters} characters \n {self.word_guessed} \n{'-'*60} \n")
    
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
            for idx in range(len(self.word)):
                if guess == self.word[idx]:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
            print(f"{'-'*60} \n H A N G M A N \n\n Good guess! {guess} is in the word. \n Number of lives: {self.num_lives} \n \n The mystery word has {self.num_letters} characters \n {self.word_guessed} \n{'-'*60} \n")        
        else: 
            self.num_lives -= 1
            print(f"{'-'*60} \n H A N G M A N \n\n Sorry, {guess} is not in the word. \n Number of lives: {self.num_lives} \n \n The mystery word has {self.num_letters} characters \n {self.word_guessed} \n{'-'*60} \n")
            


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
                break
            
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break
        
          
play_game(word_list)



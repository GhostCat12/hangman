import random

word_list = ['cherry' , 'watermelon' , 'mango' , 'strawberry' , 'banana' ]


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word)) #needs fix
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list()
    
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.word_guessed[self.word.index(guess)] = guess
            self.num_letters -= 1        
        else: 
            print(f"Sorry, {guess} is not in the word. Try again.") 


    def ask_for_input(self):
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

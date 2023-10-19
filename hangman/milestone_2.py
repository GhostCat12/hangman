import random

# create list of words called word_list
word_list = ['cherry' , 'watermelon' , 'mango' , 'strawberry' , 'banana' ]
print(word_list)

# computer chooses random word from word_list
word = random.choice(word_list)
print(word)

# function to check if user guess is valid
def is_valid_input() :
    global guess 
    while True : 
        if len(guess) == 1 and guess.isalpha() == True :
            print('Good guess!')
            break
        else : 
            print('Try again!')
            guess = input('Guess a single letter : ')

            
guess = input('Guess a single letter : ')
is_valid_input()
print(f"your guess is {guess}")
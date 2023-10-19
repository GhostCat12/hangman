import random

# create list of words called word_list
word_list = ['cherry' , 'watermelon' , 'mango' , 'strawberry' , 'banana' ]
print(word_list)

# computer chooses random word from word_list
word = random.choice(word_list)
print(word)

# milestone 3 valid input checks from task 1 already implemented in milestone 2 during optimisation in task 6
# removed is_valid_input function and ammended code to follow milestone 3 instructions   

while True :
    guess = input('Guess a single alphabetical letter : ')
    if len(guess) == 1 and guess.isalpha() == True :
        break
    else : 
        print("Invalid letter. Please, enter a single alphabetical character.")


if guess in word :
    print(f"Good guess! {guess} is in the word.")
else : 
    print(f"Sorry, {guess} is not in the word. Try again.")   


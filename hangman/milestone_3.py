# milestone 3 valid input checks from task 1 already implemented in milestone 2 during optimisation in task 6
# removed is_valid_input function and ammended code to follow milestone 3 instructions   
 
while True :
    guess = input('Guess a single alphabetical letter : ')
    if len(guess) == 1 and guess.isalpha() == True :
        break
    else : 
        print("Invalid letter. Please, enter a single alphabetical character.")




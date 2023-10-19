import random

word_list = ['cherry' , 'watermelon' , 'mango' , 'strawberry' , 'banana' ]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Guess a single letter : ')

if len(guess) == 1 and guess.isalpha() == True :
    print('Good guess!')
else : 
    print('Try again!')
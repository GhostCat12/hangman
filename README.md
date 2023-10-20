# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### How to run the game



### How it works!
1. Computer randomly chooses a word from a given word list
2. User inputs 1 alphabetical letter as a guess 
3. Computer runs checks to ensure input is valid (only 1 character long and in the alphabet)
4. Computer checks whether the guessed letter is inside the word:
    - If the guessed letter is correct, then it fills the empty spaces of the word to guess. The computer updates the number of remaining letters to guess. 
    - If the guessed letter is incorrect, the computer reduces the number of lives by 1   
5. If number of letters left to guess is 0 and number of lives is greater than 0, you have won the game! :) 
Otherwise, if number of lives deplete to 0, before guessing the word, then you have lost the game. :(





### License information : 
NU General Public License (GPL) v3.0


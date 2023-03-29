#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

# Set up the game
CN_Shows = ['Baby Looney Tunes','Beyblade series','Ben 10','Dexter\'s Laboratory','Dragon Ball Z','Naruto','Oswald','Pokémon','Popeye the Sailor','Scooby-Doo, Where Are You!','Tom and Jerry',]
#CN_Shows is a list of shows from which one will get selected randomly
word = random.choice(CN_Shows) # to select word randomly
Shows_guessed = [] 
guesses_left = 5

# Display the game state
def display_game_state():
    print('Guess the Cartoon Network show :- ', end='')
    for letter in word:
        if letter in Shows_guessed:
            print(letter, end=' ')
        else:
            print('*', end=' ')
    print('\nGuesses left:', guesses_left)
    print('Shows_guessed:', ', '.join(Shows_guessed))# The join() method takes all items in an iterable and joins them here seperated by comma(,)


# Play the game
while True:
    display_game_state()
    guess = input('Guess the Cartoon Network show: ').lower()# .lower() to covert all inputs to lower case
    if guess in Shows_guessed:
        print('You already guessed that Show!') #to avoid repetation
    elif guess in word:
        Shows_guessed.append(guess)
        if set(word) == set(Shows_guessed):
            print('Congratulations, you won!')
            break
    else:
        Shows_guessed.append(guess)
        guesses_left -= 1
        if guesses_left == 0:
            print('Sorry, you lost!!!!!. The word was', word)
            break


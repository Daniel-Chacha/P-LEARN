# a guessing game

import random


while True:
    guess=int(input('Guess the coin toss.Enter 1 for Head or 0 for Tail:  '))
    toss=random.randint(0,1)
    #print(toss)

    if guess==toss:
        print('Congrats! You guessed correctly')
        break
    else:
        print('Nop! Guess Again')

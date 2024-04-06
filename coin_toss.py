# a guessing game

import random


while True:
    guess=int(input('Guess the coin toss.Enter head or tail:  '))
    toss=random.randint(0,1)
    #print(toss)

    if guess==toss:
        print('Congrats! You guessed correctly')
        break
    else:
        print('Nop! Guess Again')

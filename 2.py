#lets play a random number gussing game

import random 
number=random.randint(1,100)
guess=None
while guess!=number:
    guess=int(input("Enter any number: "))
    if guess>number:
        print("TOO HIGH")
    elif guess<number:
        print("TOO low")
    else:
        print("You win....")




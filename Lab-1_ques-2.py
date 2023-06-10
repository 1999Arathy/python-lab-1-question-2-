#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random

random_number = random.randrange(0,9)
x = int(random_number+1)
user_guess = int(input("guess a number between 1 and 10"))
if(x == user_guess):
    print("You gussed exactly correct")
elif(x > user_guess):
    print("You gussed a lower number")
else:
    print("You gussed greater value")
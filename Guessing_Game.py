# This script is an interactive guessing game, which will ask the user to guess a number between 1 and 99.
'''
We are using the random module with the randint function to get a random number. 
The script also contains a while loop, 
which make the script run until the user guess the right number.
'''
import random
number = random.randint(1, 99)
guess = int(input(" Guess Any Number :- "))
while True:
    print("Your guessing number is {} ".format(guess))
    
    if number > guess:
        print(" Opps : You number is Smaller than {}\n".format(number))
        if (number - guess) <=5:
            print("Wow : Your too close")
            guess = int(input(" Try Again"))
        else:
            guess = int(input(" Please try again with another number :- "))

    elif number < guess:
        print(" Opps : You number is Greater than {}\n".format(number))
        if (guess - number) <=5:
            print("Wow : Your too close")
            guess = int(input(" Try Again"))
        else:
            guess = int(input(" Please try again with another number :- "))
    
    else:
        print(" Congratullations,  You guessed right number")
        print("Your number {} and system number {} both has matched".format(guess, number))
        break
    print()
    
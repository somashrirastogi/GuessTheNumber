import random
def title():
    print("Guess the number challenge")
    print("You have to guess the numbers chosen randomly from 1 to 99")
def playGame():
    g=0
#taking random no.
    n = random.randint(1, 99)
#input from user
    guess = int(input("Enter any number from 1 to 99\n"))
    while n != "guess":

        if guess < n:
            print("Too low")
            guess = int(input("Enter an integer from 1 to 99: \n"))
        elif guess > n:
            print("Too high")
            guess = int(input("Enter an integer from 1 to 99: \n"))
        else:
            print("you guessed it!")
            break

# calling functions
title()
playGame()

# Nicole Ni, MSCH-C220
import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"
number = random.randrange(1,10)
life = 5
while life > 0:
    guess = input("Guess a number from 1 to 10, you have " + str(life) + " chances to guess: ")
    if guess.isnumeric() == True:
        guess = int(guess)
        if guess == number:
            print("Great job! You got the cookie!")
            print("The number was " + str(number))
            break
        elif guess > number:
            print("Guess lower?")
            life -= 1
        elif guess < number:
            print("Guess higher?")
            life -= 1
    else: print("Please enter a NUMBER!")
else :
    print("Aww! You ran out of your chances!")
    print("The number was " + str(number))



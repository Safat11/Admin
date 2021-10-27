
import random

guessNumber = int(input("Enter your guess between 1 to 5 : "))
randomNumber = random.randint(1,5)

if guessNumber == randomNumber :
    print("You have won")

else :
    print("you have lost")

    print("Random number was : ",randomNumber)

###
# To be continue : for X in range(n,n) :

from random import randint

for X in range(1,6) :

    guessNumber = int(input("Enter your guess between 1 to 9 : "))
    randomNumber = randint(1,9)

    if guessNumber == randomNumber :
        print("You have won")

    else :
         print("you have lost")

         print("Random number was : ",randomNumber)

from random import *

def guessingGame(): 
    randNum = randint(1, 100)
    while True:
        userGuess = int(input("guess the number between 1 to 100: "))
        while userGuess != randNum:
            if userGuess > randNum: 
                print("Too high, try again.")
                break
            elif userGuess < randNum:
                print("Too low, try again.")
                break
        if userGuess == randNum:
            print("Congrats!")
            guessingGame()
guessingGame()
              

    

    




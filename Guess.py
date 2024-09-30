# --// Vairables & Services \\ --
import random #Importing the library random to use throughout the program
import time # Importing the library time to pause the program and replay after a specific time
userInput = int(input("Please enter a number to guess: ")) # Requesting the client enters a number

randomInt = random.randint(0,100) # Rqandomly generating the number and storing it in randomInt
#Continue = True
randomInt = int(randomInt) # Casting the vairable to a integer 
print(randomInt) # printing the random number for testing purposes

# --// Main Code \\ --

while userInput != randomInt: # Looping the main program until the userInput is the same as the random number
    if userInput < randomInt: # Checking if the userinput is less than the random nymber
        print("Number is less than. Guess again.")
        userInput = int(input("Please enter another guess:")) # Looping question
        #Continue = False
    elif userInput > randomInt: # Checking if the userinput it greater than the random number
        print("Number is too high. Guess again.")
        userInput = int(input("Please enter another guess:")) # looping questiom
        #Continue = False
    elif userInput == randomInt: # checking if the number is the same as the random number
        print("You Guessed the correct number!")
        time.sleep(0.5) # pausing the program for 0.5 seconds and then resuming
        quit() # ending the program
    else:     # Failsafe - if the program has an error it wont crash but will recall the loop.
        print("ERROR - There was a problem please try again.") 
        userInput = int(input("Please enter another guess:"))
        #Continue = False
print("You have Guessed the correct Number.")
    
    
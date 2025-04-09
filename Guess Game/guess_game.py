# Task 2: 
# Guess the Number Game

import random
def guess_game():
    print("Welcome to the Guessing Game!") 
    print("I have selected a number between 1 and 100.")
    # Generate a random number between 1 and 100
    num = random.randint(1, 100)
    attempts = 0
    flag = True
    while flag == True:
        try:
            # Get player's guess
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts +=1
        
        if guess == num:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            x = input("Do you want to play again press y/n ")
            if (x.lower() == 'y'):
                num = random.randint(1,100)
                attempts = 0
                continue
            else:
                flag = False
        elif guess < num:
            print("Too lower! Try Again.")
        else:
            print("Too higher! Try Again.")        
    print("Thank you for playing the game!")
guess_game()

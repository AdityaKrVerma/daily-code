## Create day03_guessing_game.py where 
## the program compares user input against a secret number

import random

def play_guessing_game():
    secret_num = random.randint(1,10)
    attempts = 0
    guess = None

    print("I am thinking of a number between 1 to 10")

    while guess != secret_num:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_num:
                print("Too low! Try again.")
            elif guess > secret_num:
                print("Too High! Try again.")
            else:
                print(f"Ahh you got me! You took {attempts} attempts :P")
        except ValueError:
            print("Invalid Input. Please enter a whole number.")

play_guessing_game()
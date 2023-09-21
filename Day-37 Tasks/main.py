# You are tasked with creating a number guessing game in Python. The game should follow these rules:
# The computer generates a random number between 1 and 100 (inclusive) and the player's task is to guess that number.
# The player has a maximum of 10 attempts to guess the correct number. After each guess, the program should provide feedback to the player: If the guess is correct,
# the program should display "Congratulations! You guessed the number."
# If the guess is too high, the program should display "Too high! Try again." and decrement the number of remaining attempts.
# If the guess is too low, the program should display "Too low! Try again." and decrement the number of remaining attempts.
# If the player doesn't guess the number within 10 attempts, the program should display "You've run out of attempts. The correct number was (correct_number}."
# You need to implement the guess_number_game() function that takes no arguments. This function should contain the game logic.
# /////////////////////////////////////////////////////////////////////////////////////


import random


def make_guess_code():

    random_number = random.randint(1, 100)

    max_attempts = 10
    attempts = max_attempts

    print("Welcome to the Number Guessing Game!")
    print(f"Guess a number between 1 and 100. You have {attempts} attempts.")

    while attempts > 0:
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if player_guess == random_number:
            print("Congratulations! You guessed the number.")
            break
        elif player_guess > random_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        attempts -= 1

    # out of attempts.
    if attempts == 0:
        print(
            f"You've run out of attempts. The correct number was {random_number}.")


# call function
make_guess_code()

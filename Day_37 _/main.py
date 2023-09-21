import random

def make_guess_code():
    random_number = random.randint(1, 100)
    max_attempts = 10
    attempts = max_attempts

    player_name = input("Enter your name: ")  # Prompt the player for their name

    print(f"Welcome, {player_name}, to the Number Guessing Game!")
    print(f"Guess a number between 1 and 100. You have {attempts} attempts.")

    while attempts > 0:
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if player_guess == random_number:
            print(f"Congratulations, {player_name}! You guessed the number.")
            break
        elif player_guess > random_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

        # Provide a hint based on the difference between the guess and the random number
        if abs(player_guess - random_number) <= 10:
            print("You're close!")
        elif abs(player_guess - random_number) <= 20:
            print("You're .")
        else:
            print("You're cold.")

        attempts -= 1

    # Out of attempts.
    if attempts == 0:
        print(f"You've run out of attempts, {player_name}. The correct number was {random_number}.")

# Call the function
make_guess_code()

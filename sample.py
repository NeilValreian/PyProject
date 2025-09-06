import random

def number_guessing_game():
    """
    A simple number guessing game for beginners.
    The computer generates a random number, and the user tries to guess it.
    """
    secret_number = random.randint(1, 20)  # Generate a random number between 1 and 20
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Your guess is too low. Try again!")
            elif guess > secret_number:
                print("Your guess is too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    number_guessing_game()
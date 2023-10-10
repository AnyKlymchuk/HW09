'''Task 1. Write a game script that randomly generates a number from a range of
1 to 100 and asks the user to guess that number in 10 tries.
The program reads the numbers entered by the user and prompts the user
whether the guessed number is greater or less than the number entered by the
user. The game must continue until the user has used 10 attempts and guessed
the number. If the user guessed the number, the program prints a
congratulatory message, and if 10 attempts have been exhausted and the user
did not have time to guess the number, then the corresponding message is
displayed.
(to perform the task, you need to import the random module,
and from it the randint() function)'''

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a random number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    while attempts < 10:
        user_guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))

        if user_guess < secret_number:
            print("The secret number is greater than your guess.")
        elif user_guess > secret_number:
            print("The secret number is less than your guess.")
        else:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts + 1} attempts.")
            break

        attempts += 1

    if attempts == 10:
        print(f"Sorry, you've exhausted all 10 attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
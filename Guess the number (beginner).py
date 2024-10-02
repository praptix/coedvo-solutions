import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < number:
            print("Try Again! You guessed too small!")
        elif guess > number:
            print("Try Again! You guessed too high!")
        else:
            print(f"Congratulations! You guessed the number {number} correctly in {10 - attempts + 1} attempts!")
            return

        attempts -= 1

    print(f"You ran out of attempts. Better luck Next Time!")

if __name__ == "__main__":
    guess_the_number()

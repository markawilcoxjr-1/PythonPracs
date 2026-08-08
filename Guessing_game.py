import random

import guess_art

def guess_game():

    game_over = False

    while not game_over:
        print(guess_art)
        print("Welcome to the Number Guessing Game!")
        print("I am thinking of a number between 1 and 100.")

        def compare():
            if user_guess == computer_guess:
                print("You win! You guessed the number.")
            elif user_guess < computer_guess:
                print("You guessed too low.")
            elif user_guess > computer_guess:
                print("You guessed too high.")

        computer_guess = random.randint(1, 100)
        difficulty = input("Choose a difficulty: 'easy' or 'hard': ").lower()

        if difficulty == "easy":
            easy = True
            num_guesses = 9

            while easy:
                user_guess = int(input("Make a guess: "))
                compare()
                num_guesses -= 1
                print(f"You have {num_guesses} guesses left.")

                if num_guesses == 0:
                    print(f"Game Over! You ran out of guesses, the answer is: {computer_guess}")
                    print("\n" * 9)
                    easy = False

        elif difficulty == "hard":
            hard = True
            num_guesses = 3

            while hard:
                user_guess = int(input("Make a guess: "))
                compare()
                num_guesses -= 1
                print(f"You have {num_guesses} guesses left.")

                if num_guesses == 0:
                    print(f"Game Over! You ran out of guesses, the answer is: {computer_guess}")
                    print("\n" * 9)
                    hard = False

        else:
            print("Invalid input. Try again.")

guess_game()
import random

while True:
    try:
        guess_amount_difficulty = int(input("Choose a difficulty level (1, 2, or 3): "))
        break
    except ValueError:
        print("Please enter a number.")
        continue


def guessing_game(difficulty: int):
    target_number = random.randint(0, 100)
    guessed_number = -1
    if difficulty == 1:
        guesses = 10
    elif difficulty == 2:
        guesses = 5
    elif difficulty == 3:
        guesses = 3

    while guessed_number != target_number:
        while True:
            try:
                guessed_number = int(input("Guess a number between 0 and 100: "))
                break
            except ValueError:
                print("Please enter a number.")
                continue

        if guesses == 0:
            return None
        guesses -= 1
        if guessed_number < target_number:
            print("Too low!")
        elif guessed_number > target_number:
            print("Too high!")
        else:
            return target_number


game_result = guessing_game(guess_amount_difficulty)

if game_result is not None:
    print(f"You won! The number was {game_result}.")
else:
    print(f"You lost! The number was {game_result}.")

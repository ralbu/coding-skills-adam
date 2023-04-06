import random

guess_amount_difficulty = input("Choose a difficulty level (1, 2, or 3): ")

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
        guessed_number = int(input("Guess a number between 0 and 100: "))
        if guesses == 0:
            return False
        guesses -= 1
        if guessed_number < target_number:
            print("Too low!")
        elif guessed_number > target_number:
            print("Too high!")
        else:
            return True

game_result = guessing_game(int(guess_amount_difficulty))
if game_result:
    print("You won!")
else:
    print("You lost!")

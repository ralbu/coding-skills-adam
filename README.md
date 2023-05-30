# Numeric types
## Exercise 1.1
- Write a function, call it `guessing_game`. Write the code in the folder *python/workout/ex1/ex1_guessing_game.py*
- When run, the function chooses a random integer between 0 and 100 (inclusive)
- Then ask the user to guess what number has been chosen
- Each time the user enters a guess, the program indicates one of the following:
    - Too high
    - Too low
    - Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to try again
- The program only exits after the user guesses correctly

**Bonus**
- At the end of the game, as the user if he/she wants to play again. If yes then start a new game, otherwise exist
- Modify the program so that it gives the user only 3 chances to guess the correct number
- Modify the program to ask the user which Level:
  - Beginner - allows 10 chances to guess the correct number
  - Intermediate - allows 5 chances to guess the correct number
  - Expert - allows 3 chances to guess the correct number

**Useful resources**

[random](https://docs.python.org/3/library/random.html#random.randint) \
[Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons) \
[f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) and (https://peps.python.org/pep-0498/) \
[for loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements) \
[input](https://docs.python.org/3/library/functions.html#input) \
[enumerate](https://docs.python.org/3/library/functions.html#enumerate) \
[reversed](https://docs.python.org/3/library/functions.html#reversed)

[comment]: <> (## Exercise 1.2)

[comment]: <> (Ex 2)

## Exercise 1.2
- Write a function, call it `my_sum`. Write the code in the folder *python/workout/ex1/ex2_my_sum.py*
- The function should take a variable number of arguments. Check the resource below for variable number of arguments
- Example to function call: *my_sum(1, 3, 4, 4)*

**Useful resources**
[Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)

## Exercise 1.3
- Write a function, call it `run_timing` that asks how long it took for you to run 5 km
- The function continues to ask how long (in minutes) it took for additional runs, until the user presses Enter
- When the user presses Enter, the function exits--but only after calculating and displaying the average time that the 5 km runs took
- Numeric inputs and outputs should all be floating-point values

***Example***
```
Enter 5 km run time: 15
Enter 5 km run time: 20
Enter 5 km run time: 10
Enter 5 km run time: <enter>
 
Average of 15.0, over 3 runs
```
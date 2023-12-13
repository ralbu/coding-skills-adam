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

## Exercise 1.4

- Write a function, call it `hex_conversion` that asks for a hexadecimal number and converts it to integer
- Don't use existing function. Iterate through every digit and convert every digit individually
- You convert from hex to decimal using the following formula:
```
Start from the rightmost digit of the hexadecimal number.
Assign a decimal value to each digit according to its position (from right to left): 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A (10), B (11), C (12), D (13), E (14), F (15).
Multiply each digit by 16 raised to the power of its position and sum the results.
For example, let's convert the hex number "1A" to decimal using the formula:

1A = (1 * 16^1) + (A * 16^0)
= (1 * 16) + (10 * 1)
= 16 + 10
= 26
```
- use the `enumerate` ([enumerate](https://docs.python.org/3/library/functions.html#enumerate)) and `reversed` ([reversed](https://docs.python.org/3/library/functions.html#reversed)) functions
- `reversed` because you need to reverse based on the above formula
- `enumerate` because you need to use the index of the digit based on the above formula
- use the `int` function which takes the second parameter as number base (16 in this case)


## Exercise 1.5
- Write a function to convert words into Pig Latin
- Use the following rules:
```
If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the word. So “air” becomes “airway” and “eat” becomes “eatway.”
If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”
```

## Exercise 1.6
- Write a function to convert a sentence into Pig Latin

## Exercise 1.7
- Write a function to convert a sentence into Ubbi Dubbi, following the rule:
``` 
For each vowel (a, e, i, o, or u) in a word, add ub before the vowel
```
***Example***

```python``` becomes ```pythubon``` and ```computer``` becomes ```cubompubutuber```


# Part 3
## Exercise 3.1 (9)
- Write a function, `first_last` that takes a sequence (string, list, or tuple) and returns the first and last elements of that sequence, in a two-element sequence of the same type
- Write a function, `even_odd_sums` that takes a list or tuple of numbers. Return a two-element list, containing (respectively) the sum of the even-indexed numbers and the sum of the odd-indexed numbers
- Write a function, `plus_minus` that takes a list or tuple of numbers. Return the result of alternately adding and subtracting numbers from each other
- Write a function, `custom_zip` that partly emulates the built-in zip function (http://mng.bz/Jyzv), taking two iterables and returning a list of tuples. Each tuple will contain one element from each of the iterables passed to the function.
- Write a function, `custom_zip_any_parameters` that partly emulates the built-in zip function (http://mng.bz/Jyzv), taking any number of iterables and returning a list of tuples. Each tuple will contain one element from each of the iterables passed to the function.



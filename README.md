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


## Exercise 3.2 (10)
- Write a function `my_sum_generic` that takes a variable number of arguments and returns the sum of those arguments. The arguments should all be of the same type (i.e., all arguments should be integers or all should be strings). If any arguments are strings, the function should return a string concatenation, not a sum.


## Exercise 3.3 (11)
- Using the `PEOPLE` dictionary, write two functions that return a list of the names of the people in the dictionary, sorted alphabetically by last name and then by first name
  - The first function `alphabetize_names_lambda` will use a lambda function to sort the list
  - The second function `alphabetize_names_itemgetter` will use the `itemgetter` function from the `operator` module to sort the list. More details at [operator.itemgetter](https://docs.python.org/3/library/operator.html#operator.itemgetter)
  

## Exercise 3.4 (12)
- Write a function `most_repeating_words` that takes a sequence of strings and returns a sequence of string that contains the greatest number of repeating words in the string.

*Example*
- When the word is `hello` it contains 2 repeating letters of `l`
- When the word is `banana` it contains 3 repeating letters of `a`
- When the words are `hello banana` it should return `banana` because it contains 3 repeating letters of `a`

You can use `Counter` from the `collections` module to count the repeating letters in the string. More details at [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter)
Pay attention to the `most_common` method [most_common](https://docs.python.org/3/library/collections.html#collections.Counter)

# Part 4

## Exercise 4.1 (14)

- Write a function, `restaurant` that asks the user to enter an order. Then check against the items in the menu dictionary.
  - If the user enters the name of a dish on the menu, the program prints the price and the running total. It then asks the user again for their order.
  - If the user enters the name of a dish not on the menu, the program tells the user that the dish is not on the menu.
  - If the user enters an empty string, the program stops prompting and prints the total amount.

*Example:*
```
Order: water
water costs 2
Total cost: 2
Order: tea
tea costs 3
Total cost: 5
Order: eggs
Sorry, no 'eggs' in menu
```

## Exercise 4.2 (15)
Complete the function `movie_tracker()` that helps you keep track of movie ratings.

- Ask the user to enter a movie title
- If they just press Enter (blank), show a final report and stop
- If they enter a movie title, ask them for a rating (1-10)
- Keep asking for more movies and ratings until they enter a blank movie title
- When they're done, show each movie and its average rating
*Example:*
```
Enter movie title: The Matrix
Enter rating: 9
Enter movie title: The Matrix
Enter rating: 8
Enter movie title: Inception
Enter rating: 10
Enter movie title: Inception
Enter rating: 9
Enter movie title: 

Movie Rating Report:
The Matrix: 8.5 average (2 ratings)
Inception: 9.5 average (2 ratings)
```

## Exercise 4.3 (16)

Write a function `dictdiff(dict1, dict2)` that compares two dictionaries and returns a new dictionary showing their differences.

- If the dictionaries are identical → return `{}` (empty dict).  
- For each differing key:
  - The result should include the key with a **list of two values**: `[value_in_dict1, value_in_dict2]`.  
  - If a key is missing in one dict, use `None` for that side.  

**Example**  
```python
dictdiff({"a": 1, "b": 2}, {"a": 1, "b": 2})
# Output: {}

dictdiff({"a": 1, "b": 2}, {"a": 1, "b": 3, "c": 4})
# Output: {"b": [2, 3], "c": [None, 4]}
```

## Exercise 4.4 (17)
Write a function `how_many_different_numbers` that takes a list of items and returns the number of different items in the list.
**Example**
```python
how_many_different_numbers([1, 1])
# Output: is 1 

how_many_different_numbers([1, 2, 2, 1])
# Output: is 2 
```
## Exercise 5.1 (18)
Write a function `get_final_line` that takes a filename as input and returns the last line of the file as a string.

Use the following documentation to learn more about filestreams:
- [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [The with statement](https://docs.python.org/3/reference/compound_stmts.html#with)

## Exercise 5.2 (19)
Write a function `password_to_dict` that reads from a Unix-style password file and returns a dictionary. The dictionary should have the username as the key and the ID are
the value.
Here's an example of the file.
```
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
```
The first field is the username and the third field is the user ID. The fields are separated by colons (`:`).
in the example above, the username is `nobody` and the user ID is `-2`.

## Exercise 5.3 (20)
Write a function `word_count` takes a filename as input and will will return four lines of output:
- Number of characters (including whitespace)
- Number of words (separated by whitespace)
- Number of lines
- Number of unique words (case sensitive, so “NO” is different from “no”)

## Exercise 5.4 (21)
Write two functions. First is `find_longest_word` takes a filename as an argument and returns the longest word found in the file.
The second function, `find_all_longest_words`, takes a directory name and returns a dict in which the keys are filenames and the values are the longest words from each file.

## Exercise 5.5 (22)
Write a function `text_to_csv` an input filename and an output filename. 
The function reads the text file which has data separated by ':' and writes its contents to a CSV file.
For each line, take the item 0 and 2 and write them to the CSV file.
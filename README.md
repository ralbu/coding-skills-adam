# Table of content
[Exercise 1](#exercise-1)\
[Exercise 2](#exercise-2)\
[Exercise 3](#exercise-3)\
[Exercise 4](#exercise-4)\
[Exercise 5](#exercise-5)\
[Exercise 6](#exercise-6)\
[Exercise 7](#exercise-7)\
[Exercise 8](#exercise-8)\
[Exercise 9](#exercise-9)\
[Exercise 10](#exercise-10)\
[Exercise 11](#exercise-11)

# Exercise 1

Given a `string`, convert it to a `lower case string`

**Example 1**

```
Input:  HeLLo

Output: hello
```

**Example 2**

```
Input:  HELLO

Output: hello
```


# Exercise 2
Enter your age and display the year you were born

**Example**

```
Input:  12

Output: You were born in 2010
```

# Exercise 3
Enter a number and display if it is `even` or `odd`

**Example 1**

```
Input:  100

Output: Even
```

**Example 2**

```
Input: 55

Output: Odd
```

# Exercise 4
Enter two numbers and multiply them.

Ask for the next two numbers.

Exit the application when typing `q` or `quit`

## Additional
Display a message if entered numbers are not integer numbers
If `q` or `quit` is entered instead of number 1 or number 2 terminate the application


# Exercise 5
Enter an integer number `N`
Find the largest number which can divide `N` by `3`.\
When N is less than 3 then the result is 0.\
When N is 3 then the result is 3.

**Example**

```
Input: 6
Output: 6

Input: 7
Output: 6

Input: 55
Output: 54
```

# Exercise 6
You have a basket with fruits.

Write the implementation for the existing functions as below:

```
list_all_fruits_in_the_basket()
```

- List all the fruits as comma separated string with the fist letter of the fruit in Upper Case.

```
does_the_basket_contain_fruit(fruit: string)
```

- Return True if the basket contains a fruit
- Return False if the basket does NOT contain a fruit

```
get_last_fruit()
```
  - Get the last fruit from the basket

```
add_fruit(fruit: string)
```
- Add a new fruit to the basket.
NOTE: this function should not change the content of the basket. It should create a copy of the existing basket

```
add_fruit_in_the_middle(fruit:string):
```
- Mom bought an orange, but she doesn't want you to see it, so she hides the orange behind the banana. \
Insert the orange fruit in the basket, so it is inserted after the banana
  
```
remove_banana_from_basket():
```
- Remove banana fruit from the basket
  
```
remove_last_two_fruits_from_basket():
```
- Remove `mango` and `dragon fruit` from the basket and return the removed fruit as a string separated by comma

```
remove_fruit(fruit: string):
```
- Remove a fruit from the basket

# Exercise 7
## Sum of all numbers
Suppose you have a natural number `N`\
Calculate the sum of all of the integers from `1` to `N`\
There are two methods you need to implement:
```
sum_of_all_numbers_using_list(number: int)
```
Calculate the sum only using list methods, like range, sum. Can you write the code as one line only?

```
sum_of_all_numbers_by_formula(number: int)
```
Use this formula to calculate the Sum
```
Sum = N(N+1) / 2
```

# Exercise 8
Implement required functionality for the below functions:
```
generate_odd_range(max_number_in_list: int)
```
- Generate a list of `Odd` numbers starting from 1 and using the provided parameter `max_number_in_lst` as the highest threshold 

```
generate_square_numbers(from_min: int, to_max: int)
```
- Generate a list of `Square numbers` using `from_min` and `to_max` as minimum and maximum values to generate the list\
Example:
```
Input: from_min = 1, to_max = 3

Output: 1, 4, 9
```

```
get_top_three()
```
- Return only the top highest three numbers from the provided list

# Exercise 9
Calculate the sum of tuples as described in the example below
```
Tuple example: [[(a, b), (c, d)], [(e, f), (g, h)]]
Result sum: (a + c + e + g), (b + d + f + h)
```

# Exercise 10
Given a number `N`, display all the prime numbers up to number `N`

**Example**
```
Input: 8
Output: 2, 3, 5, 7
```

# Exercise 11
Given an array of dictionaries with Game Players and their score, calculate the average score of players with the name which
starts with the same letter

**Example**
```
Input: 
        players = [
            {'name': 'James', 'score': 200},
            {'name': 'Mary', 'score': 100},
            {'name': 'John', 'score': 100}
        ]
Output: 
    {
     'J': 150, 
     'M': 100
     }
```
J = 150 because first letter is J from James and John and add they score 200 + 100 and divide two 2
M = 100 because only Mary starts with M and the score is 100
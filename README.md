# Table of content
[Exercise1](#exercise-1)
[Exercise2](#exercise-2)
[Exercise3](#exercise-3)
[Exercise4](#exercise-4)
[Exercise5](#exercise-5)
[Exercise6](#exercise-6)

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
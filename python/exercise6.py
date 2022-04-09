import string
from math import trunc

def list_all_fruits_in_the_basket():
    basket = ['apple', 'banana', 'mango', 'dragon fruit']
    to_return = ''
    for i in basket:
        to_return += i.capitalize()
        if basket.index(i) != len(basket)-1:
            to_return += ', '
    return to_return

def does_the_basket_contain_fruit(fruit: string):
    basket = ['apple', 'banana', 'mango', 'dragon fruit']

    if fruit.lower() in basket:
        return True
    else:
        return False

def get_last_fruits():
    basket = ['apple', 'banana', 'mango', 'dragon fruit']
    return basket[-1]

def add_fruit(fruit: string):
    basket = ['apple', 'banana', 'mango', 'dragon fruit']
    basket.append(fruit.lower())
    return basket

def add_fruit_in_the_middle(fruit: string):
    basket = ['apple', 'banana', 'mango', 'dragon fruit']
    mid_basket = trunc(len(basket)/2)       
    basket.insert(mid_basket, fruit)
    return basket

def remove_banana_from_basket():
    basket = ['apple', 'banana', 'mango', 'dragon fruit']
    basket.remove('banana')
    return basket

def remove_last_two_fruits_from_basket(basket):
    basket.remove(basket[-1])
    basket.remove(basket[-1])
    return basket

def remove_fruit(fruit: string):
    basket = ['apple', 'banana', 'mango', 'dragon fruit']
    basket.remove(fruit)
    return basket
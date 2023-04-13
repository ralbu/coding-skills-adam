def generate_odd_range(max_number_in_list: int):
    return list(range(1,max_number_in_list,2))

def generate_square_numbers(from_min: int, to_max: int):
    numbers = list(range(from_min, to_max+1))
    return [i ** 2 for i in numbers]

def get_top_three():
    list_numbers = [3, 1, 20, 7, 66, 8, 30, 81, 43, 11, 98, 1, 5]
    list_numbers.sort()
    top_three = [list_numbers[-1], list_numbers[-2], list_numbers[-3]]
    return top_three

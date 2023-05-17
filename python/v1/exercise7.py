def sum_of_all_numbers_using_list(number: int):
    list_of_numbers = list(range(0, number + 1))
    sum = 0
    for n in list_of_numbers:
        sum += n
    return sum

def sum_of_all_numbers_by_formula(number: int):
    # Sum = N(N+1) / 2
    sum = 0
    sum = number*(number + 1) / 2
    return sum


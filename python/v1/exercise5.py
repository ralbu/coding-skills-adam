def highest_divisor_of_three(no: int):
    if no < 3:
        return 0
    elif no % 3 == 0:
        return no
    elif no % 3 == 1:
        return no - 1
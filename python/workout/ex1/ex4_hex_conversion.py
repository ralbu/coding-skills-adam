# Start from the rightmost digit of the hexadecimal number.
# Assign a decimal value to each digit according to its position (from right to left): 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A (10), B (11), C (12), D (13), E (14), F (15).
# Multiply each digit by 16 raised to the power of its position and sum the results.
# For example, let's convert the hex number "1A" to decimal using the formula:
#
# 1A = (1 * 16^1) + (A * 16^0)
# = (1 * 16) + (10 * 1)
# = 16 + 10
# = 26

def convert_hex(hex_num):
    letter_digits = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    digits = []
    calc = [0, 0]
    for digit in hex_num:
        if digit.upper() in letter_digits:
            digits.append(int(letter_digits[digit.upper()]))
        else:
            digits.append(int(digit))

    for digit in digits:
        print(type(digit))

    calc[0] = digits[0] * 16 ** 1
    calc[1] = digits[1] * 16 ** 0

    return sum(calc)


converted_hex = convert_hex('A1')
print(converted_hex)
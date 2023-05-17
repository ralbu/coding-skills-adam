def sum_roll_dice():
    dice_rolls = [(3, 8), (11, 7), (38, 2),
                  (51, 19), (43, 2), (21, 10)]

    sum1 = 0
    sum2 = 0
    for i in dice_rolls:
        sum1 += i[0]
    for i in dice_rolls:
        sum2 += i[1]

    return sum1, sum2

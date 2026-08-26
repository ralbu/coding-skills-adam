menu = {"tea": 3, "coffee": 4, "water": 2, "ice cream": 3, "cake": 5}


def restaurant():
    running_total = 0
    while (order := input("Order: ").lower()) != "":
        if order in menu.keys():
            cost = menu[order]
            running_total += cost
            print(f"{order} costs {cost}")
            print(f"Total cost: {running_total}")
        else:
            print(f"Sorry, no '{order}' in menu")
            continue


if __name__ == "__main__":
    restaurant()

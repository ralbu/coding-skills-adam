import string


display_message = "Type 'q' or 'quit' to terminate "

print(display_message)

def check_int(str_var: string):
    try:
        int(str_var)
        return True
    except:
        print(str_var, ' is not an integer.')
        return False


def quit_application(var):
    return 'q' == var or 'quit' == var

while True:
    n1 = input("Enter first number ")

    if quit_application(n1):
        break

    if not check_int(n1):
        continue

    n2 = input("Enter second number ")

    if quit_application(n2):
        break

    if not check_int(n2):
        continue

    print(int(n1)*int(n2))
    print('')
    print('')
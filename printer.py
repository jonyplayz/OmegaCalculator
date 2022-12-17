def welcome_message():
    print("welcome to the Omega Calculator\n")


def goodbye_message():
    print("thank you for using the Omega Calculator, goodbye")


def show_specific_index_of_exception(eq, operator):
    """
    this function prints the exact place where there was an error
    :param eq: the whole equation
    :param operator: the operator where the error happened
    """
    print("the error was here:")
    print(eq)
    for c in eq:
        if c == operator:
            print('^')
            break
        else:
            print(" ", end='')

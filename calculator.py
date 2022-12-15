from OmegaCalculator.the_brain import *
from OmegaCalculator.input_check import *
from OmegaCalculator.custom_exceptions import equation_exception


def welcome_message():
    print("welcome to the Omega Calculator\n")


def goodbye_message():
    print("thank you for using the Omega Calculator, goodbye")


def start_calculator():
    """
    this program controls the input and output of the calculator
    :var: does_continue - a flag that indicates if the user wants to calculate another equation or quit the calculator
                eq - a string which gets the inputted equation from the user
                operators - a map that saves the operators and their strength
                error_flag - a flag that indicates if an error has occurred while inputting the equation
                not_minus - a flag that indicates if we passed all the first minuses in an equation (this flag is used for exception checking)
                has_operation - a flag that indicates if the current equation has an operator in it or not (this flag is used for exception checking)
                has_content -  a flag that indicates if there is something other then operators in the equation
    """
    welcome_message()
    does_continue = True
    while does_continue:
        error_flag = False
        operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
        print("please enter your equation bellow or enter 'quit' to quit\n")
        try:
            eq = input()  # getting the inputted equation to eq while checking for EOFError exception
        except EOFError:
            print("an error has occurred, it was caused by inputting 'end of file', this error is fatal. please restart the calculator")
            break

        if not error_flag:
            if eq == "quit":  # if the user has inputted "quit" then we need to exit the calculator
                goodbye_message()
                does_continue = False
                break
            if does_continue:
                not_minus = False
                has_operator = False
                has_content = False
                for c in eq:  # this loop checks if we have an operator in the equation
                    if c not in operators:
                        has_operator = True
                    if not_minus:
                        if c in operators:
                            has_operator = True

                    if c != '-' and not not_minus:
                        not_minus = True
                        if c in operators:
                            has_operator = True
                if not has_operator:  # if the equation doesnt have an operator then check for exceptions in it
                    try:
                        eq_check(eq)
                    except equation_exception as error:  # an excpetion if the equation doesnt have an operator and has something which is not a number
                        print(error)
                        error_flag = True
                    except emptyEq_exception as error:  # an exception to check if the equation is empty
                        print(error)
                        error_flag = True
                if not not_minus:   # if the equation is just minuses then raise an exception
                    print("\nan error has occurred, it was caused by the whole equation not being valid")
                    error_flag = True
                if not_minus and not has_content:
                    print("\nan error has occurred, it was caused by the whole equation not being valid")
                    error_flag = True
                eq = eq.replace(" ", "")  # removing all the spaces in the equation
            if not error_flag:  # if we didn't encounter an error then calculate the equation
                answer = calculate(eq)
                if answer != "quit":  # if no errors were detected during the calculation then print the answer
                    print(f"the answer is: {answer}")

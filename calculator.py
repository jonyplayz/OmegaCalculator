from OmegaCalculator.the_brain import *
from OmegaCalculator.input_check import *
from OmegaCalculator.custom_exceptions import equation_exception


def welcome_message():
    print("welcome to the Omega Calculator\n")


def goodbye_message():
    print("thank you for using the Omega Calculator, goodbye")


def controller():
    welcome_message()
    does_continue = True
    while does_continue:
        operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
        print("please enter your equation bellow or enter 'quit' to quit\n")
        error_flag = False
        eq = input()
        if eq == "quit":
            goodbye_message()
            does_continue = False
        if does_continue:
            not_minus = False      # flag to say if we passed all minuses at the first of the equation
            has_operator = False
            for c in eq:
                if not_minus:
                    if c in operators:
                        has_operator = True

                if c != '-' and not not_minus:
                    not_minus = True
                    if c in operators:
                        has_operator = True
            if not has_operator:
                try:
                    eq_check(eq)
                except equation_exception as error:
                    print(error)
                    error_flag = True

            answer = calculate(eq)
            if answer != "quit" and not error_flag:
                print(f"the answer is: {answer}")

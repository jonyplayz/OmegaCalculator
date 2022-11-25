from functions import *
from input_check import *


def calculate(eq):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    found_operator = True
    op1 = ""
    op2 = ""
    current_operator = ""
    op1_index = 0
    op2_index = 0
    while found_operator:
        found_operator = False
        for c in eq:
            if c in operators:
                if current_operator == "":
                    current_operator = c
                else:
                    if operators[c] > operators[current_operator]:
                        current_operator = c
                    else:
                        result = operations(op1, op2, current_operator)
                        eq = eq[:op1_index] + result + eq[op2_index:]



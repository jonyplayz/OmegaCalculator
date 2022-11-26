from functions import *
from input_check import *


def calculate(eq):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    found_operator = True
    op1 = ""
    op2 = ""
    current_operator = ""
    op1_index = 0
    op2_index = 1
    result = ""
    while found_operator:
        found_operator = False
        for c in eq:
            if result == "":
                if c in operators:
                    found_operator = True
                    if current_operator == "":
                        current_operator = c
                    else:
                        if operators[c] > operators[current_operator]:
                            current_operator = c
                            op1 = op2
                            op2 = ""
                            op1_index = op2_index
                            while eq[op2_index] not in operators:
                                op2_index += 1
                            op2_index += 1
                        else:
                            result = operations(op1, op2, current_operator)
                            while eq[op2_index] not in operators:
                                op2_index += 1
                            eq = eq[:op1_index] + str(result) + eq[op2_index:]

                else:
                    if not found_operator:
                        op2_index += 1
                        op1 = op1 + c
                    else:
                        op2 = op2 + c

        if result == "" and found_operator:
            result = operations(op1, op2, current_operator)
            while op2_index != len(eq) - 1:
                op2_index += 1
            eq = eq[:op1_index] + str(result)

        result = ""
        op1 = ""
        op2 = ""
        op1_index = 0
        op2_index = 1
        current_operator = ""

    return eq

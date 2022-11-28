from OmegaCalculator.functions import *
from OmegaCalculator.input_check import *


def calculate(eq):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    found_operator = True
    while found_operator:
        op1 = ""
        op2 = ""
        current_operator = ""
        op1_index = 0
        op2_index = 1
        result = ""
        found_operator = False
        for c in eq:
            if result == "":
                if c == '(':
                    result = sograim(eq, op2_index)
                    op1_index = op2_index
                    while eq[op2_index] != ')':
                        op2_index+=1
                    if eq[0] != '(':
                        eq = eq[:op1_index] + str(result) + eq[op2_index+1:]
                    else:
                        eq = eq[:op1_index-1] + str(result) + eq[op2_index+1:]
                    found_operator = True

                elif c in operators:
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

    return eq


def sograim(sograimStr, start):
    tempStr = sograimStr[start:]

    opening = start
    counter = start
    endedFlag = False
    ending = start
    for c in tempStr:
        if not endedFlag:
            if c == ')':
                endedFlag = True
                ending = counter
            if c == '(' and not endedFlag:
                opening = counter
            counter += 1
    #print(str(opening) + " " + str(ending))
    if ending == opening:
        raise TypeError("close brackets is missing. please restart the calculator")
    if sograimStr[0] != '(':
        tempStr = sograimStr[opening+1:ending]
    else:
        tempStr = sograimStr[opening:ending]
    result = calculate(tempStr)
    start = opening
    return result


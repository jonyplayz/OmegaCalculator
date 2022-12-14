from OmegaCalculator.custom_exceptions import *


def check_input(op1, op2, operator):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    decimal_counter1 = 0
    decimal_counter2 = 0
    for c in op1:
        if c == '.':
            decimal_counter1 += 1
    if decimal_counter1 > 1:
        raise operand1_exception()
    for c in op2:
        if c == '.':
            decimal_counter2 += 1
    if decimal_counter2 > 1:
        raise operand2_excpetion()

    if operator == "~":
        if op2 == '':
            raise_correct_exception(operator)
        for c in op2:
            if '.' < c < '0' or c < '.' or c > '9':
                raise operand2_excpetion()
        if op1 not in operators and op1 != '':
            raise_correct_exception(operator)
        if decimal_counter2 == 1:
            op2 = float(op2)
        else:
            op2 = int(op2)
    elif operator == "!":
        if decimal_counter1 == 1:
            raise operand1_exception()
        if op1[0] == '-':
            raise operand1_exception()
        if op1 == '':
            raise_correct_exception(operator)
        for c in op1:
            if '.' < c < '0' or c < '.' or c > '9':
                raise operand1_exception()
        if op2 not in operators and op2 != '':
            raise_correct_exception(operator)
        op1 = int(op1)

    # elif operator == "!":
    #     if decimal_counter1 == 1:
    #         raise TypeError("cant do factorial with decimal number")
    #
    #     for c in op1:
    #         if '.' < c < '0' or c < '.' or c > '9':
    #             raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")
    #     if op2 not in operators and op2 != '':
    #         raise TypeError("can only have operators after a factorial operator. please restart the calculator")
    #     op1 = int(op1)

    else:
        if op1 == '':
            raise_correct_exception(operator)
        if op2 == '':
            raise_correct_exception(operator)
        for c in op1:
            if ('.' < c < '0' or c < '.' or c > '9') and c != '-':
                raise operand1_exception()
        for c in op2:
            if ('.' < c < '0' or c < '.' or c > '9') and c != '-':
                raise operand2_excpetion()
        if decimal_counter1 == 1:
            op1 = float(op1)
        else:
            op1 = int(op1)
        if decimal_counter2 == 1:
            op2 = float(op2)
        else:
            op2 = int(op2)

    return [op1, op2]


def eq_check(eq):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    for c in eq:
        if ('.' < c < '0' or c < '.' or c > '9') and c not in operators:
            raise equation_exception()


def raise_correct_exception(operator):
    if operator == "+":
        raise plus_exception()
    if operator == "-":
        raise minus_exception()
    if operator == "*":
        raise mul_exception()
    if operator == "/":
        raise div_exception()
    if operator == "^":
        raise pow_exception()
    if operator == "%":
        raise mod_exception
    if operator == "$":
        raise max_exception()
    if operator == "&":
        raise min_exception()
    if operator == "@":
        raise avg_exception()

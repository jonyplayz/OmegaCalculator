from OmegaCalculator.custom_exceptions import *


def check_input(op1, op2, operator):
    """
    this program validates the left and right operands according to the operator
    :param op1: the left operand
    :param op2: the right operand
    :param operator: the operator
    :var:   operators - a map of a;; the operators and their strength
            decimal_counter1 - a counter of the number of '.' in the left operand
            decimal_counter2 - a counter of the number of '.' in the right operand

    :return: returns the left and right operands after converting them to int/float
    """
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    decimal_counter1 = 0
    decimal_counter2 = 0
    for c in op1:   # goes over the left operand and counts how many '.' he has
        if c == '.':
            decimal_counter1 += 1
    if decimal_counter1 > 1:    # if the left operand has more then 1 dot them call an exception
        raise operand1_exception()
    for c in op2:   # goes over the right operand and counts how many '.' he has
        if c == '.':
            decimal_counter2 += 1
    if decimal_counter2 > 1:    # if the right operand has more then 1 dot them call an exception
        raise operand2_excpetion()

    if operator == "~":
        if op2 == '':   # if we got the negative operator and the right operand is empty then its an operator exception
            raise_operator_exception(operator)
        for c in op2:   # this loop goes over the right operand and checks if any chars are not valid
            if '.' < c < '0' or c < '.' or c > '9':
                raise operand2_excpetion()
        if op1 not in operators and op1 != '':  # if the left operand is not an operator and also not empty then raise an operator exception
            raise_operator_exception(operator)
        if decimal_counter2 == 1:   # if there is a decimal dot then convert to float, else to int
            op2 = float(op2)
        else:
            op2 = int(op2)
    elif operator == "!":
        if decimal_counter1 == 1:   # if there is a decimal dot raise an exception about the left operand
            raise operand1_exception()
        if op1[0] == '-':   # if the left operand is negeitve then raise an exception
            raise operand1_exception()
        if op1 == '':   # if the left operand is empty then raise an operator exception
            raise_operator_exception(operator)
        for c in op1:   # this loop goes over the left operand and checks if any chars are not valid
            if '.' < c < '0' or c < '.' or c > '9':
                raise operand1_exception()
        if op2 not in operators and op2 != '':  # if the right operand is not an operator and also not empty then raise an operator exception
            raise_operator_exception(operator)
        op1 = int(op1)  # converts the left operand to int

    else:
        if op1 == '':   # if the left operand is empty raise an operator exception
            raise_operator_exception(operator)
        if op2 == '':   # if the right operand is empty raise an operator exception
            raise_operator_exception(operator)

        if operator == '^': # if the operator is pow and base is negative and the exponent is a decimal then raise complex exception
            if op1[0] == '-':
                if decimal_counter2 > 0:
                    raise complex_exception()

        for c in op1:   # this loop goes over the left operand and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9') and c != '-':
                raise operand1_exception()
        for c in op2:   # this loop goes over the right operand and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9') and c != '-':
                raise operand2_excpetion()
        if decimal_counter1 == 1:   # if there is a decimal dot then convert to float, else to int
            op1 = float(op1)
        else:
            op1 = int(op1)
        if decimal_counter2 == 1:   # if there is a decimal dot then convert to float, else to int
            op2 = float(op2)
        else:
            op2 = int(op2)

    return [op1, op2]


def eq_check(eq):
    """
    this program checks the equation at the start to check for end cases
    :param eq: the starting equation
    :var:   operators - a map that holds the operators and their strength

    """
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    if eq == "":    # if the equation is empty throw an exception
        raise emptyEq_exception()
    else:
        for c in eq:    # this loop goes over the equation and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9') and c not in operators:
                raise equation_exception()


def raise_operator_exception(operator):
    """
    this program raises an operator exception according to the operator
    :param operator: an operator as char
    """
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

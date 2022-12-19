from custom_exceptions import *
from config import *


def check_input(op1, op2, operator):
    """
    this function validates the left and right operands according to the operator
    :param op1: the left operand
    :param op2: the right operand
    :param operator: the operator
    :var:   operators - a map of a;; the operators and their strength
            decimal_counter1 - a counter of the number of '.' in the left operand
            decimal_counter2 - a counter of the number of '.' in the right operand

    :return: returns the left and right operands after converting them to int/float
    """
    decimal_counter1 = 0
    decimal_counter2 = 0
    for c in op1:  # goes over the left operand and counts how many '.' he has
        if c == '.':
            decimal_counter1 += 1
    if decimal_counter1 > 1:  # if the left operand has more then 1 dot them call an exception
        raise operand1_exception()
    for c in op2:  # goes over the right operand and counts how many '.' he has
        if c == '.':
            decimal_counter2 += 1
    if decimal_counter2 > 1:  # if the right operand has more then 1 dot them call an exception
        raise operand2_exception()

    if operator == "~":
        if op2 == '':  # if we got the negative operator and the right operand is empty then its an operator exception
            raise_operator_exception(operator)
        for c in op2:  # this loop goes over the right operand and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9') and (c != '-' or (c == '-' and len(op2) == 1) and c != 'e'):
                raise operand2_exception()
        if op1 not in operators and op1 != '':  # if the left operand is not an operator and also not empty then raise an operator exception
            raise_operator_exception(operator)
        if decimal_counter2 == 1:  # if there is a decimal dot then convert to float, else to int
            op2 = float(op2)
        else:
            op2 = int(op2)
    elif operator == "!":
        if decimal_counter1 == 1:  # if there is a decimal dot raise an exception about the left operand
            raise operand1_exception()
        if op1[0] == '-':  # if the left operand is negative then raise an exception
            raise operand1_exception()
        if op1 == '':  # if the left operand is empty then raise an operator exception
            raise_operator_exception(operator)
        for c in op1:  # this loop goes over the left operand and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9')  and c != 'e':
                raise operand1_exception()
        if op2 not in operators and op2 != '':  # if the right operand is not an operator and also not empty then raise an operator exception
            raise_operator_exception(operator)
        op1 = int(op1)  # converts the left operand to int

    elif operator == "#":
        if op1 == '':  # if the left operand is empty then raise an operator exception
            raise_operator_exception(operator)
        for c in op1:  # this loop goes over the left operand and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9') and c != 'e':
                raise operand1_exception()
        if op2 not in operators and op2 != '':  # if the right operand is not an operator and also not empty then raise an operator exception
            raise_operator_exception(operator)
        if decimal_counter1 == 1:  # if there is a decimal dot then convert to float, else to int
            op1 = float(op1)
        else:
            op1 = int(op1)

    else:
        if op1 == '':  # if the left operand is empty raise an operator exception
            raise_operator_exception(operator)
        if op2 == '':  # if the right operand is empty raise an operator exception
            raise_operator_exception(operator)

        if operator == '^':  # if the operator is pow and base is negative and the exponent is a decimal then raise complex exception
            if op1[0] == '-':
                if decimal_counter2 > 0:
                    raise complex_exception()
        if operator == '/':
            not_zero = False
            str_holder = op2
            if op2[0] == '-' and len(op2) > 1:
                str_holder = op2[1:]
            for c in str_holder:
                if c != '0':
                    not_zero = True
            if not not_zero:
                raise divideByZero_exception()

        for c in op1:  # this loop goes over the left operand and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9') and c != '-' and c != 'e':
                raise operand1_exception()
        for c in op2:  # this loop goes over the right operand and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9') and c != '-' and c != 'e':
                raise operand2_exception()
        if decimal_counter1 == 1:  # if there is a decimal dot then convert to float, else to int
            op1 = float(op1)
        else:
            op1 = int(op1)
        if decimal_counter2 == 1:  # if there is a decimal dot then convert to float, else to int
            op2 = float(op2)
        else:
            op2 = int(op2)

    return [op1, op2]


def eq_check(eq, not_minus, has_content):
    """
    this function checks the equation at the start to check for end cases
    :param eq: the starting equation
    :param not_minus: a flag that indicates if there is something other than minuses in the original equation
    :param has_content: a flag that indicates if the original equation has something other than operators
    :var:   operators - a map that holds the operators and their strength

    """
    if eq == "":  # if the equation is empty throw an exception
        raise emptyEq_exception()
    else:
        for c in eq:  # this loop goes over the equation and checks if any chars are not valid
            if ('.' < c < '0' or c < '.' or c > '9') and c not in operators and c != '(' and c != ')':
                raise equation_exception()
    if not not_minus:  # if the equation is just minuses then raise an exception
        raise equation_exception()
    if not_minus and not has_content:  # if the equation is only operators then raise an exception
        raise equation_exception()


def raise_operator_exception(operator):
    """
    this function raises an operator exception according to the operator
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
    if operator == "#":
        raise digitSum_exception()
    if operator == "~":
        raise neg_exception()

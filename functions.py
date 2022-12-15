from math import pow
from input_check import *


def operations(op1, op2, operator):
    """
    this program checks for errors in the operands and sends them to the correct operator function
    :param op1: left operand
    :param op2: right operand
    :param operator: the operator

    :return: returns None if there was an error, returns the result of the calculation
    """
    try:
        list = check_input(op1, op2, operator)  # validates the left and right operands
        op1 = list[0]  # puts the left operand after conversion to int/float
        op2 = list[1]  # puts the right operand after conversion to int/float
    except plus_exception as error:
        print(error)
        return None
    except minus_exception as error:
        print(error)
        return None
    except mul_exception as error:
        print(error)
        return None
    except div_exception as error:
        print(error)
        return None
    except mod_exception as error:
        print(error)
        return None
    except pow_exception as error:
        print(error)
        return None
    except max_exception as error:
        print(error)
        return None
    except min_exception as error:
        print(error)
        return None
    except avg_exception as error:
        print(error)
        return None
    except complex_exception as error:
        print(error)
        return None
    except operand1_exception as error:
        l = [error, "which is", "'" + op1 + "'"]  # this list is used to print all the error at once
        print(*l)
        return None
    except operand2_excpetion as error:
        l = [error, "which is", "'" + op2 + "'"]  # this list is used to print all the error at once
        print(*l)
        return None

    if operator == "+":  # calls the operator function by the operator
        return add(op1, op2)
    if operator == "-":
        return sub(op1, op2)
    if operator == "*":
        return mul(op1, op2)
    if operator == "/":
        return div(op1, op2)
    if operator == "^":
        return pow_override(op1, op2)
    if operator == "%":
        return mod(op1, op2)
    if operator == "$":
        return max(op1, op2)
    if operator == "&":
        return min(op1, op2)
    if operator == "@":
        return avg(op1, op2)
    if operator == "~":
        return neg(op2)
    if operator == "!":
        return factorial(op1)


"""
all of the functions bellow are operator functions
"""


def add(op1, op2):
    return op1 + op2


def sub(op1, op2):
    return op1 - op2


def mul(op1, op2):
    return op1 * op2


def div(op1, op2):
    return op1 / op2


def pow_override(op1, op2):
    return pow(op1, op2)


def mod(op1, op2):
    return op1 % op2


def max(op1, op2):
    if op1 > op2:
        return op1
    else:
        return op2


def min(op1, op2):
    if op1 < op2:
        return op1
    else:
        return op2


def avg(op1, op2):
    return (op1 + op2) / 2


def neg(op1):
    return op1 * -1


def factorial(op1):
    num = 1
    sum = 1
    while num != op1 + 1:
        sum = sum * num
        num += 1
    return sum

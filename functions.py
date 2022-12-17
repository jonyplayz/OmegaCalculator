from math import pow
from input_check import *
from printer import show_specific_index_of_exception


def operations(op1, op2, operator, eq):
    """
    this function checks for errors in the operands and sends them to the correct operator function
    :param op1: left operand
    :param op2: right operand
    :param operator: the operator
    :param eq: the current full equation

    :return: returns None if there was an error,else, returns the result of the calculation
    """
    try:
        return_list = check_input(op1, op2, operator)  # validates the left and right operands
        op1 = return_list[0]  # puts the left operand after conversion to int/float
        op2 = return_list[1]  # puts the right operand after conversion to int/float
    except plus_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except minus_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except mul_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except div_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except mod_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except pow_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except max_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except min_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except avg_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except neg_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except complex_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except digitSum_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except divideByZero_exception as error:
        print(error)
        show_specific_index_of_exception(eq, operator)
        return None
    except operand1_exception as error:
        return_list = [error, "which is", "'" + op1 + "'"]  # this list is used to print all the error message at once
        print(*return_list)
        show_specific_index_of_exception(eq, operator)
        return None
    except operand2_exception as error:
        return_list = [error, "which is", "'" + op2 + "'"]  # this list is used to print all the error message at once
        print(*return_list)
        show_specific_index_of_exception(eq, operator)
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
        return maximum(op1, op2)
    if operator == "&":
        return minimum(op1, op2)
    if operator == "@":
        return avg(op1, op2)
    if operator == "~":
        return neg(op2)
    if operator == "!":
        return factorial(op1)
    if operator == "#":
        return digit_sum(op1)


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


def maximum(op1, op2):
    if op1 > op2:
        return op1
    else:
        return op2


def minimum(op1, op2):
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
    result = 1
    while num != op1 + 1:
        result = result * num
        num += 1
    return result


def digit_sum(op1):
    result = 0
    op1_string = str(op1)
    op1_string = op1_string.replace(".", "")
    op1 = int(op1_string)
    while op1 > 0:
        result += (op1 % 10)
        op1 /= 10
        op1 = int(op1)
    return result

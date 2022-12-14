from math import pow
from input_check import *


# def operations(op1, op2, operator):
#     return {
#         '+': add(op1, op2),
#         '-': sub(op1, op2),
#         '*': mul(op1, op2),
#         '/': div(op1, op2),
#         '^': pow_override(op1, op2),
#         '%': mod(op1, op2),
#         '$': max(op1, op2),
#         '&': min(op1, op2),
#         '@': avg(op1, op2),
#         '~': neg(op2),
#         '!': factorial(op1),
#     }[operator]


def operations(op1, op2, operator):
    try:
        list = check_input(op1, op2, operator)
        op1 = list[0]
        op2 = list[1]
    # except equation_exception as error:
    #     print(error)
    #     return None
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
    except operand1_exception as error:
        l = [error, "which is", "'" + op1 + "'"]
        print(*l)
        return None
    except operand2_excpetion as error:
        l = [error, "which is", "'" + op2 + "'"]
        print(*l)
        return None

    if operator == "+":
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

from math import pow


def operations(op1, op2, operator):
    if operator == "+":
        return add(op1, op2)
    if operator == "-":
        return sub(op1, op2)
    if operator == "*":
        return mul(op1, op2)
    if (operator == "/"):
        return div(op1, op2)
    if (operator == "^"):
        return pow_override(op1, op2)
    if (operator == "%"):
        return mod(op1, op2)
    if (operator == "$"):
        return max(op1, op2)
    if (operator == "&"):
        return min(op1, op2)
    if (operator == "@"):
        return avg(op1, op2)
    if (operator == "~"):
        return neg(op2)
    if (operator == "!"):
        return add(op1)


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
    if (op1 > op2):
        return op1
    else:
        return op2


def min(op1, op2):
    if (op1 < op2):
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
    while num != op1:
        sum = sum * num
        num += 1
    return sum

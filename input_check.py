def check_input(op1, op2, operator):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    decimal_counter1 = 0
    decimal_counter2 = 0
    for c in op1:
        if c == '.':
            decimal_counter1 += 1
    if decimal_counter1 > 1:
        raise TypeError("one or zero decimal dot is allowed. please restart the calculator")
    for c in op2:
        if c == '.':
            decimal_counter2 += 1
    if decimal_counter2 > 1:
        raise TypeError("one or zero decimal dot is allowed. please restart the calculator")

    if operator == "~":
        for c in op2:
            if '.' < c < '0' or c < '.' or c > '9':
                raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")
        if op1 not in operators:
            raise TypeError("can only have operators after a negative operator. please restart the calculator")
        if decimal_counter2 == 1:
            op2 = float(op2)
        else:
            op2 = int(op2)
    elif operator == "!":
        if decimal_counter1 == 1:
            raise TypeError("cant do factorial with decimal number")

        for c in op1:
            if '.' < c < '0' or c < '.' or c > '9':
                raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")
        if op2 not in operators and op2 != '':
            raise TypeError("can only have operators after a factorial operator. please restart the calculator")
        op1 = int(op1)
    else:
        for c in op1:
            if '.' < c < '0' or c < '.' or c > '9':
                raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")
        for c in op2:
            if '.' < c < '0' or c < '.' or c > '9':
                raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")
        if decimal_counter1 == 1:
            op1 = float(op1)
        else:
            op1 = int(op1)
        if decimal_counter2 == 1:
            op2 = float(op2)
        else:
            op2 = int(op2)

    return [op1, op2]

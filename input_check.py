def check_input(op1, op2, operator):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    decimal_counter = 0
    for c in op1:
        if c == '.':
            decimal_counter+=1
    if decimal_counter > 1:
        raise TypeError("one or zero decimal dot is allowed. please restart the calculator")
    decimal_counter = 0
    for c in op2:
        if c == '.':
            decimal_counter+=1
    if decimal_counter > 1:
        raise TypeError("one or zero decimal dot is allowed. please restart the calculator")

    decimal_counter = 0

    if operator == "~":
        for c in op2:
            if c == '.':
                decimal_counter = 1
            if '.' < c < '0' or c < '.' or c > '9':
                raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")
        if op1 not in operators:
            raise TypeError("can only have operators after a negative operator. please restart the calculator")
        if decimal_counter == 1:
            op2 = float(op2)
        else:
            op2 = int(op2)
    elif operator == "!":
        for c in op1:
            if '.' < c < '0' or c < '.' or c > '9':
                raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")
        if op2 not in operators:
            raise TypeError("can only have operators after a factorial operator. please restart the calculator")
    else:
        for c in op1:
            if '.' < c < '0' or c < '.' or c > '9':
                raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")
        for c in op2:
            if '.' < c < '0' or c < '.' or c > '9':
                raise TypeError("only numbers and decimal dot is accepted. please restart the calculator")

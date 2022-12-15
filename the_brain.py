from OmegaCalculator.functions import *
from OmegaCalculator.input_check import *
from OmegaCalculator.custom_exceptions import *


def calculate(eq):
    """
    this program calculates the equation while also handling any exceptions that might pop up

    :param eq: an equation in string type

    :var: eq - an equation in string type
                operators - a map that saves the operators and their strength
                found_operator -  a flag which indicates if an operator has been found yet or not
                op1 - a variable that saves the current left operand in type string
                op2 - a variable that saves the current right operand in type string
                current_operator - a variable that saves the current operator that needs to be calculated in type string
                op1_index - an index that saves the place in the equation where the left operand starts
                op2_index - an index that saves the place in the equation where the right operand starts
                result - a variable that saves the result from the various calculations in the equation
                string_index - an index that saves the current place in the equation
                eq_len - a variable that saves the current length of the equation
                compressed_minus - a flag that indicates if we have compressed minuses in the current iteration
                current_char - a variable that saves the current char that we are on from the equation

    :return: the solution to the equation
    """
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    found_operator = True
    while found_operator:  # this loop ends when no operator is detected in the current equation
        op1 = ""
        op2 = ""
        current_operator = ""
        op1_index = 0
        op2_index = 1
        result = ""
        found_operator = False

        string_index = 0
        eq_len = len(eq)
        compressed_minus = False

        while string_index < eq_len:  # this loop ends when we went over all the current equation string

            current_char = eq[string_index]  # gets the current char from the equation
            if True:
                if result == "":  # if we didn't calculate anything already then continue
                    if current_char == '(':
                        try:
                            result = sograim(eq,
                                             op2_index)  # calling a program that calculates the equation in the brackets nad putting it in result
                        except emptyBrackets_exception as error:
                            print(error)
                            result = "quit"

                        if result == "quit":  # if result is "quit" then we encountered an error and the calculation should stop
                            return result
                        op1_index = op2_index  # op1_index getting updated with the correct index
                        while eq[op2_index] != ')':  # increasing op2_index until we reach the closing brackets
                            op2_index += 1
                        if eq[0] != '(':  # if the equation doesnt start with opening brackets
                            eq = eq[:op1_index] + str(result) + eq[op2_index + 1:]
                        else:  # if the equation start with opening brackets
                            eq = eq[:op1_index - 1] + str(result) + eq[op2_index + 1:]
                        found_operator = True

                    elif current_char in operators:  # checks if the current char is an operator
                        found_operator = True
                        if current_operator == "":  # if we didn't encounter an operator yet then true
                            if current_char == '-' and op1 == "":  # checks if we encounter a minus that is a number sign
                                found_operator = False

                                list = minus_reduction(0, eq,
                                                       op1)  # calls minus reduction program to reduct all the minuses correctly
                                eq = list[0]  # put the returned equation into eq
                                op1 = list[1]  # put the returned first char of the lef operand to op1
                                op2_index += 1
                                compressed_minus = True

                            elif op2 == "" and current_char == '-':  # checks if we encounter a minus that is an operator
                                list = minus_reduction(op2_index - 1, eq, op1)
                                eq = list[0]  # put the returned equation into eq
                                current_operator = eq[
                                    op2_index - 1]  # puts the given operator after the minus redaction into current_operator
                                compressed_minus = True
                            else:  # if we didnt encounter a operator yet and its not a vareation of minus then put it in current_operator
                                current_operator = current_char

                        else:
                            if op2 == "" and current_char == '-' and current_operator != '!':  # if we encountered
                                # an operator already and its not an operator with one operand and we see a minus

                                list = minus_reduction(op2_index, eq, op1)
                                eq = list[0]  # puts the returned equation into eq
                                if eq[op2_index] == '-':  # if the right operand starts with a minus then add it
                                    op2 = eq[op2_index]
                                compressed_minus = True

                            else:  # if we encounter another operator after already seeing one before
                                if operators[current_char] > operators[
                                    current_operator]:  # if the operator we just encountered is stronger than the
                                                        # operator we saw before

                                    current_operator = current_char  # current_operator gets the stronger operator
                                    op1 = op2  # the left operand gets the right operand
                                    op2 = ""  # resetting the right operand
                                    op1_index = op2_index  # updating the index of the start of the left operand
                                    if eq[op2_index] == '-':  # if the first char of the left operand is minus then increase op2_index
                                        op2_index += 1
                                    while eq[op2_index] not in operators:  # this loop gets op2_index to point to the start of the right operand
                                        op2_index += 1
                                    op2_index += 1

                                else:   # if the operator we encountered now is weaker than current_operator
                                    result = operations(op1, op2, current_operator) # calculates with the current left operand, right operand and current_operator
                                    if result is None:  # if we got None then there has been an error and the calculation of the equation should stop
                                        eq = "quit"
                                    else:
                                        if eq[op2_index] == '-' and (compressed_minus or (current_operator != '!')):    # the right operand is negetive and we compressed minuses
                                                                                                                        # or its not a one sided operator than increase op2_index
                                            op2_index += 1
                                        while eq[op2_index] not in operators:   # increases op2_index so it will point to the end of the right operand
                                            op2_index += 1
                                        if current_operator == '~': # if the current operator is '~' then we need to put brackets on the result because it turns into a number sign
                                            eq = eq[:op1_index] + '(' + str(result) + eq[op2_index] + ')' + eq[
                                                                                                            op2_index + 1:] # update the equation with the current result of the calculation
                                        else:
                                            eq = eq[:op1_index] + str(result) + eq[op2_index:]  # update the equation with the current result of the calculation

                    else:   # if we don't see an operator
                        if not found_operator:  # if we didnt found an operator yet then add the char to the left operand and increase op2_index
                            op2_index += 1
                            op1 = op1 + current_char
                        else:   # if we found an operator then add the char to the right operand
                            op2 = op2 + current_char

            string_index += 1   # increases the string index
            eq_len = len(eq)    # updates the length of the equation into eq_len
            compressed_minus = False    # resets the compressed_minus flag

        if result == "" and found_operator: # if we didn't calculate anything but found an operator
            result = operations(op1, op2, current_operator) # calculates with the current left operand, right operand and current_operator
            if result is None:  # if we got None then there has been an error and the calculation of the equation should stop
                eq = "quit"
            else:
                eq = eq[:op1_index] + str(result)   # update the equation with the current calculation

    return eq


def sograim(sograim_str, start):
    """
    this program handles the use of brackets in an equation by finding the equation inside the brackets and calculating it
    :param sograim_str: the whole equation
    :param start: the index of the start of the opening brackets
    :var: temp_str - a variable that gets the equation from the starting of the opening brackets
                opening - index of the opening bracket
                ending - index of the closing bracket
                counter - a counter that helps updating the indexes of opening and closing
                ended_flag - a flag that indicates if we encountered a closing bracket
    :return: the calculated equation inside the brackets
    """
    temp_str = sograim_str[start:]  # puts the equation from the starting of the opening brackets

    opening = start # resets the opening bracket index
    counter = start # resets the counter
    ended_flag = False
    ending = start  # resets the closing bracket index
    for c in temp_str:  # this loop goes over the splitted equation to find the most inner brackets
        if not ended_flag:  # if we didnt find an ending bracket
            if c == ')':
                ended_flag = True
                ending = counter
            if c == '(' and not ended_flag: # if we see another opening bracket and we didnt see an ending bracket then update the opening index
                opening = counter
            counter += 1
    if ending-1 == opening:   # if the brackets are empty then throw an error
        raise emptyBrackets_exception()
    if sograim_str[0] != '(':   # if the original equation doesnt start with opening brackets
        temp_str = sograim_str[opening + 1:ending]  # put in temp_str the equation in the brackets
    else:   # if the original equation start with opening brackets
        temp_str = sograim_str[opening:ending]  # put in temp_str the equation in the brackets
    result = calculate(temp_str)    # calculate the equation inside the brackets
    return result


def minus_reduction(start, eq, op1):
    """
    this program redacts minuses accordingly
    :param start: index of the first minus
    :param eq: the equation
    :param op1: the left operand
    :var: start_minus_index - an index of the start of the minuses
            holder_str - a holder that holds the equation but stripped from the first minus
            end_flag -  a flag that indicates if we reached the end of the minuses
            end_minus_index - an index of the end of the minuses

    :return: the equation after the reduction and the first char of the left operand
    """
    start_minus_index = start
    holder_str = eq[start_minus_index:]
    end_flag = False
    end_minus_index = start_minus_index - 1
    for ch in holder_str:   # a loop that goes over the stripped equation and finds the end of the minuses
        if ch != '-':
            end_flag = True
        if not end_flag:
            end_minus_index += 1
    if (end_minus_index - start_minus_index) % 2 != 0:  # checks if we got even or odd number of minuses
        if op1 == "":  # if there is even number of minuses and its not an operator
            eq = eq[:start_minus_index] + eq[end_minus_index + 1:]  # update the equation with the reduction
            op1 = op1 + eq[0]   # update the left operand
        else:   # if there is even number of minuses and its an operator
            eq = eq[:start_minus_index] + '+' + eq[end_minus_index + 1:]    # update the equation with the reduction and sign change
    else:
        if op1 == "":  # if there is odd number of minuses and its not an operator
            eq = eq[:start_minus_index + 1] + eq[end_minus_index + 1:]  # update the equation with the reduction
            op1 = op1 + eq[0]   # update the left operand
        else:   # if there is odd number of minuses and its an operator
            eq = eq[:start_minus_index] + '-' + eq[end_minus_index + 1:]    # update the equation with the reduction and sign change

    return [eq, op1]

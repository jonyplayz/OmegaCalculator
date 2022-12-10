from OmegaCalculator.functions import *
from OmegaCalculator.input_check import *


def calculate(eq):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
    found_operator = True
    while found_operator:
        op1 = ""
        op2 = ""
        current_operator = ""
        op1_index = 0
        op2_index = 1
        result = ""
        found_operator = False
        skipping_counter_end = 0
        skipping_counter_start = 0
        holder = 0
        print(eq + " this is eq in the beginning")

        for c in eq:

            if not op2_index < skipping_counter_end:
                if result == "":
                    if c == '(':
                        result = sograim(eq, op2_index)
                        op1_index = op2_index
                        while eq[op2_index] != ')':
                            op2_index += 1
                        if eq[0] != '(':
                            eq = eq[:op1_index] + str(result) + eq[op2_index + 1:]
                        else:
                            eq = eq[:op1_index - 1] + str(result) + eq[op2_index + 1:]
                        found_operator = True

                    elif c in operators:
                        found_operator = True
                        if current_operator == "":
                            if c == '-' and op1 == "":
                                found_operator = False

                                list = minus_reduction(0, eq, op1, op2, operators, current_operator,
                                                       op1_index, skipping_counter_end)
                                eq = list[0]
                                skipping_counter_end = list[1]
                                op1 = list[2]
                                op2_index += 1
                                skipping_counter_start = list[3]
                                # op2 = op2 + eq[op2_index]
                                # else:
                                #     eq = minus_reduction(op2_index - 1, eq, op1, op2, operators, current_operator,
                                #                          op1_index)
                                #     op1 = op1 + eq[0]
                                # minus_skip = True
                            # op2_index += 1

                            else:
                                if op2 == "" and c == '-':
                                    list = minus_reduction(op2_index - 1, eq, op1, op2, operators, current_operator,
                                                           op1_index, skipping_counter_end)
                                    eq = list[0]
                                    skipping_counter_end = list[1] + 1
                                    skipping_counter_start = list[3]
                                    current_operator = eq[op2_index - 1]
                                else:
                                    current_operator = c

                        else:
                            if op2 == "" and c == '-':
                                # print("minus in second")
                                if current_operator == '!':
                                    result = operations(op1, op2, current_operator)
                                    while eq[op2_index] not in operators:
                                        op2_index += 1
                                    eq = eq[:op1_index] + str(result) + eq[op2_index:]
                                else:
                                    # op2_index += 1
                                    print("op2_index in mid eq" + str(op2_index))
                                    if holder == 0:
                                        list = minus_reduction(op2_index, eq, op1, op2, operators, current_operator,
                                                               op1_index, skipping_counter_end)
                                        eq = list[0]
                                        if eq[op2_index] == '-':
                                            op2 = eq[op2_index]

                                    else:
                                        list = minus_reduction(holder, eq, op1, op2, operators, current_operator,
                                                               op1_index, skipping_counter_end)
                                        eq = list[0]
                                        op2 = eq[op2_index]
                                        op2_index = holder
                                    skipping_counter_end = list[1]
                                    skipping_counter_start = list[3]

                            else:
                                if operators[c] > operators[current_operator]:

                                    current_operator = c
                                    op1 = op2
                                    op2 = ""
                                    #op2_index = skipping_counter_start
                                    holder = skipping_counter_start

                                    print("this is holder " + str(holder))
                                    if eq[holder] == '-':
                                        holder += 1
                                    while eq[holder] not in operators:
                                        holder += 1
                                    holder += 1

                                    if op1_index == 0 and skipping_counter_start != 0:
                                        op1_index = holder - skipping_counter_start
                                        op1_index = holder - op1_index
                                    else:
                                        op1_index = holder


                                else:
                                    result = operations(op1, op2, current_operator)
                                    holder = skipping_counter_start
                                    while eq[holder] != c:
                                        holder += 1
                                    eq = eq[:op1_index] + str(result) + eq[holder:]

                    else:
                        if not found_operator:
                            op2_index += 1
                            op1 = op1 + c
                        else:
                            op2 = op2 + c
            else:
                print("skipped")
                print(op2_index)
                op2_index += 1

        if result == "" and found_operator:
            result = operations(op1, op2, current_operator)
            # if len(eq) - 1 != 0:
            #     while op2_index != len(eq) - 1:
            #         op2_index += 1
            eq = eq[:op1_index] + str(result)

    return eq


def sograim(sograimStr, start):
    tempStr = sograimStr[start:]

    opening = start
    counter = start
    endedFlag = False
    ending = start
    for c in tempStr:
        if not endedFlag:
            if c == ')':
                endedFlag = True
                ending = counter
            if c == '(' and not endedFlag:
                opening = counter
            counter += 1
    # print(str(opening) + " " + str(ending))
    if ending == opening:
        raise TypeError("close brackets is missing. please restart the calculator")
    if sograimStr[0] != '(':
        tempStr = sograimStr[opening + 1:ending]
    else:
        tempStr = sograimStr[opening:ending]
    result = calculate(tempStr)
    start = opening
    return result


def minus_reduction(start, eq, op1, op2, operators, current_operator, op1_index, skipping_counter_end):
    start_minus_index = start
    holder_str = eq[start_minus_index:]
    print(holder_str + " this is holder str and op1 " + op1)
    end_flag = False
    end_minus_index = start_minus_index - 1
    skipping_counter_end = 0
    for ch in holder_str:
        if ch != '-':
            end_flag = True
        if not end_flag:
            end_minus_index += 1
    print(str(end_minus_index) + " " + str(start_minus_index))
    if (end_minus_index - start_minus_index) % 2 != 0:
        if op1 == "":  # if there is even number of minuses and its not an operator
            eq = eq[:start_minus_index] + eq[end_minus_index + 1:]
            op1 = op1 + eq[0]
            print(eq + " this is eq without operat")
        else:
            eq = eq[:start_minus_index] + '+' + eq[end_minus_index + 1:]
            print(eq + " this is eq with plus")
        # print(eq + " soozgi" + str(start_minus_index) + " " + str(end_minus_index))
    else:
        if op1 == "":  # if there is odd number of minuses and its not an operator
            eq = eq[:start_minus_index + 1] + eq[end_minus_index + 1:]
            op1 = op1 + eq[0]
        else:
            eq = eq[:start_minus_index] + '-' + eq[end_minus_index + 1:]
            # skipping_counter = 1
        # eq = eq[:start_minus_index] + '-' + eq[end_minus_index + 1:]
        # print(eq + " this is eq sith minus")

        # print(eq + "Ezoogi")
    # end_flag = False
    # op2 = op2 + eq[start_minus_index]
    # for ch in eq[start_minus_index + 1:]:
    #     if ch in operators:
    #         end_flag = True
    #     if not end_flag:
    #         op2_index += 1
    #         op2 = op2 + ch
    # result = operations(op1, op2, current_operator)
    # eq = eq[:op1_index] + str(result) + eq[op2_index + 1:]
    skipping_counter_end += end_minus_index
    skipping_counter_start = start_minus_index
    return [eq, skipping_counter_end, op1, skipping_counter_start]

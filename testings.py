import pytest
from pytest import *
from the_brain import *
from input_check import *
from custom_exceptions import equation_exception
from config import *
from printer import *


@pytest.mark.skip
def test_start_calculator():
    """
    this function is a copy of the start_calculator function. it was made to enable testing with pytest
    :var: does_continue - a flag that indicates if the user wants to calculate another equation or quit the calculator
                eq - a string which gets the inputted equation from the user
                operators - a map that saves the operators and their strength
                error_flag - a flag that indicates if an error has occurred while inputting the equation
                not_minus - a flag that indicates if we passed all the first minuses in an equation (this flag is used for exception checking)
                has_operation - a flag that indicates if the current equation has an operator in it or not (this flag is used for exception checking)
                has_content -  a flag that indicates if there is something other then operators in the equation
    """
    # welcome_message()
    # does_continue = True
    # while does_continue:
    error_flag = False
    eq = ""
    # print("please enter your equation bellow or enter 'quit' to quit\n")
    try:
        eq = input()  # getting the inputted equation to eq while checking for EOFError exception
    except EOFError:
        print(
            "an error has occurred, it was caused by inputting 'end of file', this error is fatal. please restart the calculator")
        error_flag = True
    if not error_flag:
        if eq == "quit":  # if the user has inputted "quit" then we need to exit the calculator
            goodbye_message()
            return None
        not_minus = False
        has_operator = False
        has_content = False
        for c in eq:  # this loop checks the equations and set the flags
            if c not in operators:
                has_content = True
            if not_minus:
                if c in operators:
                    has_operator = True
            if c != '-' and not not_minus:
                not_minus = True
                if c in operators:
                    has_operator = True
        if not has_operator:  # if the equation doesnt have an operator then check for exceptions in it
            try:
                eq_check(eq, not_minus, has_content)
            except equation_exception as error:  # an exception if the equation doesnt have an operator and
                # has something which is not a number
                print(error)
                error_flag = True
            except emptyEq_exception as error:  # an exception to check if the equation is empty
                print(error)
                error_flag = True
        eq = eq.replace(" ", "")  # removing all the spaces in the equation
        eq = eq.replace("\t", "")  # removing all the tabs in the equation
    if not error_flag:  # if we didn't encounter an error then calculate the equation
        answer = calculate(eq)
        if answer != "quit":  # if no errors were detected during the calculation then print the answer
            print(f"the answer is: {answer}")


"""
test methods starts bellow
"""


def test_simple_syntax_error(capsys, monkeypatch):
    eq_list = ["2+*2", "2^*3", "2$/4", "2~-~4"]
    answers_list = ["mul\nthe error was here:\n2+*2\n  ^\n", "pow\nthe error was here:\n2^*3\n ^\n",
                    "max\nthe error was here:\n2$/4\n ^\n",
                    "operand 2 which is '-'\nthe error was here:\n2~-~4\n ^\n"]
    answer_list_index = 0
    for strings in eq_list:
        monkeypatch.setattr('builtins.input', lambda: strings)
        test_start_calculator()
        stdout, stderr = capsys.readouterr()
        assert stdout == '\nan error has occurred, it was caused by ' + answers_list[answer_list_index]
        answer_list_index += 1


def test_jibrish_equation_error(capsys, monkeypatch):
    jibrish_equation = "kjhsdhjhsgkdjh"
    monkeypatch.setattr('builtins.input', lambda: jibrish_equation)
    test_start_calculator()
    stdout, stderr = capsys.readouterr()
    assert stdout == '\nan error has occurred, it was caused by the whole equation not being valid\n'


def test_empty_equation_error(capsys, monkeypatch):
    empty_equation = ""
    monkeypatch.setattr('builtins.input', lambda: empty_equation)
    test_start_calculator()
    stdout, stderr = capsys.readouterr()
    assert stdout == '\nan error has occurred, it was caused by the equation being empty\n'


def test_white_spaces_equation_error(capsys, monkeypatch):
    white_spaces_list = [" ", "\t", "\v", "\n", "\r", "\f", "   "]
    answers_list = ["the whole equation not being valid\n", "the whole equation not being valid\n",
                    "the whole equation not being valid\n",
                    "the whole equation not being valid\n", "the whole equation not being valid\n",
                    "the whole equation not being valid\n",
                    "the whole equation not being valid\n"]
    answer_list_index = 0
    for strings in white_spaces_list:
        monkeypatch.setattr('builtins.input', lambda: strings)
        test_start_calculator()
        stdout, stderr = capsys.readouterr()
        assert stdout == '\nan error has occurred, it was caused by ' + answers_list[answer_list_index]
        answer_list_index += 1


def test_simple_equation(capsys, monkeypatch):
    equation_list = ["2+2", "9-3", "5*-2", "4/0.5", "16^0.5", "12%2", "8$9", "8&9", "10@2", "-~4", "5!", "-123#"]
    answers_list = ["4\n", "6\n", "-10\n", "8.0\n", "4.0\n", "0\n", "9\n", "8\n", "6.0\n", "4\n", "120\n", "-6\n"]
    answer_list_index = 0
    for strings in equation_list:
        monkeypatch.setattr('builtins.input', lambda: strings)
        test_start_calculator()
        stdout, stderr = capsys.readouterr()
        assert stdout == 'the answer is: ' + answers_list[answer_list_index]
        answer_list_index += 1


def test_complex_equation(capsys, monkeypatch):
    equation_list = ["120#+-54*33-6!/(4^3)-6",
                     "69##!#!##-437/(15-6)^3",
                     "2^(~3--12)+15$6&44&3",
                     "2---3! + 4!-~3 - 09 * 0.001 * 10 ^ 3 * (2-1)",
                     "5!# * 3 @ 1 + -1 ^ 4 + (2) * (4 ^ -~-2.00)",
                     "60^2--(---3000)/5^2#!",
                     "158#+---3^43#---(123*8/6!)",
                     "4+52#!^2*4&5$8---1000",
                     "3*5%2+65/(-47#$-2+6)",
                     "-36#*(47#-554#)####+12",
                     "(654*4)$99^3/5!#!#-~23",
                     "(4+6)*756#--8^4-(555#)",
                     "~17$30*3.3&5.5-(12#-2!)",
                     "(5%2+300@10)-    3^2/9+55&3",
                     "30*0.1$2--~5+(10!*2-30)%5-(30/5+1)",
                     "6!-3^3*2+  (~2/~1+2#)*1-3%2+1",
                     "100&99/33+1.1^2-(3!+~1)%2+7*7",
                     "5$(4*-123#^2 /12.7@5.3)-100%(12*2.5)"]
    answers_list = ["-1796.25\n",
                    "8.400548696844993\n",
                    "515.0\n",
                    "13.999999999999998\n",
                    "7.125\n",
                    "3480.0\n",
                    "-2174.366666666667\n",
                    "203211804.0\n",
                    "19.25\n",
                    "39\n",
                    "2983746839.0\n",
                    "4261.0\n",
                    "98.0\n",
                    "158.0\n",
                    "48.0\n",
                    "670.0\n",
                    "52.21\n",
                    "6.0\n"]
    answer_list_index = 0
    for strings in equation_list:
        monkeypatch.setattr('builtins.input', lambda: strings)
        test_start_calculator()
        stdout, stderr = capsys.readouterr()
        assert stdout == 'the answer is: ' + answers_list[answer_list_index]
        answer_list_index += 1

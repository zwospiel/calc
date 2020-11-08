# Idea::::?:::!

## TODO for GUI: most double operators (except *-) are not allowed as input
## TODO: sqrt sqrt oder sin sin wuerde probleme machen -> ebenfalls gui solving? 
# ; rueckwaerts ????
#?: position_of_result auf 0 setzen; wie ausserhalb der Methode?
#?: a cute tea expert looks at your code, what you do?
#?: multiplication: can if-flow be tidied up for better viewing? 
# how can i improve the arrangement of my arguments?

import math
# global index to be used by the recursion; will get dynamically changed
# by length of the result
position_of_result = 0

# parseulation handler
def solve(operator, one, two):
    # case of single operator; not giving 0 into the function 
    # (for empty second operator) 
    #  because i want len(two) to be 0 in replace_formula_with_result
    if two == "":
        two = 0
    one = float(one)
    two = float(two)
    if operator == "sqrt":
        return str(sqrt(one))
    if operator == "sin":
        return str(sin(one))
    if operator == "^":
        return str(one**two)
    if operator == "*":
        return str(one*two)
    if operator == "/":
        return str(one/two)
    if operator == "+":
        return str(one+two)
    if operator == "-":
        return str(one-two)
    # potential reconversion to int somewhere to avoid dirty .0 ints


def replace_formula_with_result(input, position, operator, one, two = ""):
    # solve operation
    result = solve(operator, one, two)
    # save latest position in the position_of_result
    currentIndex = position
    # we remove the operator and number(s) and instead insert the result
    # want to restart after the result
    position = position-len(one)-len(operator)-len(two)+len(result) 
    input = input[0:position-len(result)] + result + input[currentIndex:] 
    # result returned in case of further operations
    return input, position, result 

def parse(input):
    global position_of_result
    position_of_result = 0
    
    validate(input)
    return main(input)
    
def main(input):
    #?: position + index too complicated?
    global position_of_result
    number1 = ""
    number2 = ""
    operator = ""
    position = 0
    
    # brackets; only here are we counting position_of_result for recursion
    while position < len(input):
        # recursion for each open bracket until first ")"
        if input[position] == "(":
            result = main(input[position_of_result+1:])
            # position_of_result is counting globally,
            # so we know where the rescursion ends 
            # and can cut up the position_of_result accordingly
            input = input[0:position] + result + input[position_of_result+1:]
            position_of_result = position_of_result \
                - (position_of_result  \
                - len(result) - position)
            position += len(result)
        elif input[position] == ")":
            position = len(input)
            position_of_result += 1
            break
        position_of_result += 1
        position += 1


    # multiplication
    # each number in the string is divided by an operator,
    # which I use to identify them

    position = 0
    found_operator = False 
    # if we have read a * or /, we will do an calculation after the next number
    # specified by found_operator = True
    
    # leading minus in the first position
    if (input[position] == "-" and number1 == "" and number2 == ""):
        number2 += "-"
        position+=1

    while position < len(input):
        # end of recursion
        if input[position] == ")":
            break
        # * or / : 
        # for found_operator = False
        if ((input[position] == "*" or input[position] == "/") 
            and not found_operator):
            number1 = number2
            number2 = ""
            operator = input[position]
            found_operator = True
        # for found_operator = True
        elif ((input[position] == "*" or input[position] == "/")
            and found_operator):
            input, position, number1 = replace_formula_with_result(
                input,
                position,
                operator,
                number1,
                number2)
            operator = input[position]
            number2 = ""
        # for *- or /- cases
        elif (input[position] == "-" and (input[position-1] == "*" 
            or input[position-1] == "/") and (position > 0)):
            number2 += "-"
        # no new * or /, resolving found_operator = True
        elif ((input[position] == "+" or input[position] == "-") 
            and found_operator):
            input, position, number1 = replace_formula_with_result(
                input,
                position,
                operator,
                number1,
                number2)
            number2 = ""
            found_operator = False
        elif ((input[position] == "+" or input[position] == "-")
            and not found_operator):
            number2 = ""
        else:
            # add current position to number if no operator
            number2 += input[position]
        position +=1
    # if last operator was * or /
    if found_operator:
        input, position, number1 = replace_formula_with_result(
            input, 
            position, 
            operator, 
            number1, 
            number2)

    number1 = ""
    number2 = ""
            
            
    # addition
    # no other operators than + or - left, so we can simply add all the numbers

    for element in input:
        # end of recursion
        if element == ")":
            break
        # minus at input[0]
        elif (element == "-" and number2 == ""):
            number2 += "-"
        # first operator which also signifies first number
        elif ((element == "+" or element == "-") and number1 == ""):
            number1 = number2
            number2 = ""
            operator = element
        # after that, we always add or subtract number2 unto number1
        elif (element == "+" or element == "-"):
            number1 = solve(operator, number1, number2)
            number2 = ""
            operator = element
        else:
            number2 += element
    # last operation
    if number1 != "" and number2 != "":
        number1 = solve(operator, number1, number2)
    # if string is a single number
    elif number2 != "":
        number1 = number2
    return number1


def validate(input):
    if type(input) is not str:
        raise TypeError("Input not a string")

    if input == "":
        raise ValueError("Input string must not empty")

    i = 0
    while i < len(input):
        if input[i] == ",":
            raise ValueError("Fractions must be divided by '.' and not ','")
        i += 1
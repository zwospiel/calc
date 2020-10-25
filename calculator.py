## TODO for GUI: most double operators (except *-) are not allowed as input
## TODO: sqrt sqrt oder sin sin wuerde probleme machen -> ebenfalls gui solving? ; rueckwaerts ????
#?: Index auf 0 setzen; wie ausserhalb der Methode?
#?: a cute tea expert looks at your code, what you do?
#?: multiplication: can if-flow be tidied up for better viewing? 
# how can i improve the arrangement of my arguments?

import math
# global index to be used by the recursion; will get dynamically changed by length of the result
index = 0

# parseulation handler
def Solver(operator, one, two):
    # case of single operator; not giving 0 into the function (for empty second operator) 
    # because i want len(two) to be 0 in inputcutter
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


def inputCutter(input, startingIndex, operator, one, two = ""):
    # solve operation
    result = Solver(operator, one, two)
    # save latest position in the index
    currentIndex = startingIndex
    # we remove the operator and number(s) and instead insert the result
    startingIndex = startingIndex-len(one)-len(operator)-len(two)+len(result) # want to restart after the result
    input = input[0:startingIndex-len(result)] + result + input[currentIndex:] 
    return input, startingIndex, result # result returned in case of further operations
    
def parse(input):
    #?: startingindex + index too complicated?
    global index
    number1 = ""
    number2 = ""
    operator = ""
    startingIndex = 0
    
    # brackets; only here are we counting index for recursion
    while startingIndex < len(input):
        if input[startingIndex] == "(":
            # recursion for each open bracket until first ")"
            result = parse(input[index+1:])
            # index is counting globally, so we know where the rescursion ends 
            # and can cut up the index accordingly
            input = input[0:startingIndex] + result + input[index+1:]
            index = index - (index  - len(result) - startingIndex)
            startingIndex += len(result)
        elif input[startingIndex] == ")":
            startingIndex = len(input)
            index += 1
            break
        index += 1
        startingIndex += 1


    # multiplication
    # each number in the string is divided by an operator, which I use to identify them

    startingIndex = 0
    go = "off" 
    # if we have read a * or /, we will do an operation after the next number
    # specified by go = "on"
    
    # leading minus in the first position
    if (input[startingIndex] == "-" and number1 == "" and number2 == ""):
        number2 += "-"
        startingIndex+=1

    while startingIndex < len(input):
        # end of recursion
        if input[startingIndex] == ")":
            break
        # * or / : 
        # for go = "off"
        if ((input[startingIndex] == "*" or input[startingIndex] == "/") and go == "off"):
            number1 = number2
            number2 = ""
            operator = input[startingIndex]
            go = "on"
        # for go = "on"
        elif ((input[startingIndex] == "*" or input[startingIndex] == "/") and go == "on"):
            input, startingIndex, number1 = inputCutter(input, startingIndex, operator, number1, number2)
            operator = input[startingIndex]
            number2 = ""
        # for *- or /- cases
        elif (input[startingIndex] == "-" and (input[startingIndex-1] == "*" or input[startingIndex-1] == "/") and (startingIndex > 0)):
            number2 += "-"
        # no new * or /, resolving go = "on"
        elif ((input[startingIndex] == "+" or input[startingIndex] == "-") and go == "on"):
            input, startingIndex, number1 = inputCutter(input, startingIndex, operator, number1, number2)
            number2 = ""
            go = "off"
        elif ((input[startingIndex] == "+" or input[startingIndex] == "-") and go == "off"):
            number2 = ""
        else:
            # add current index to number if no operator
            number2 += input[startingIndex]
        startingIndex +=1
    # if last operator was * or /
    if go == "on":
        input, startingIndex, number1 = inputCutter(input, startingIndex, operator, number1, number2)

    number1 = ""
    number2 = ""
            
            
    # addition
    # no other operators than + or - left, so we can simply add all the numbers

    for element in input:
        # end of recursion
        if element == ")":
            break
        # minus at first index
        elif (element == "-" and number2 == ""):
            number2 += "-"
        # first operator which also signifies first number
        elif ((element == "+" or element == "-") and number1 == ""):
            number1 = number2
            number2 = ""
            operator = element
        # after that, we always add or subtract number2 unto number1
        elif (element == "+" or element == "-"):
            number1 = Solver(operator, number1, number2)
            number2 = ""
            operator = element
        else:
            number2 += element
    # last operation
    if number1 != "" and number2 != "":
        number1 = Solver(operator, number1, number2)
    # if string is a single number
    elif number2 != "":
        number1 = number2
    return number1
## TODO for GUI: most double operators (except *-) are not allowed as input
## TODO: sqrt sqrt oder sin sin wuerde probleme machen -> ebenfalls gui solving? ; rueckwaerts ????
#?: Index auf 0 setzen; wie ausserhalb der Methode?
#?: a cute tea expert looks at your code, what you do?
#?: multiplication: can if-flow be tidied up for better viewing? how can i improve the arrangement of my arguments?

import math

index = 0


def Solver(operator, one, two):
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
    
def inputCutter(input, startingIndex, operator, one, two = ""):
    result = Solver(operator, one, two)
    currentIndex = startingIndex
    startingIndex = startingIndex-len(one)-len(operator)-len(two)+len(result)
    input = input[0:startingIndex-len(result)] + result + input[currentIndex:] 
    return input, startingIndex, result
    
def calc(input):
    ### startingindex + index too complicated?
    global index
    number1 = ""
    number2 = ""
    operator = ""
    startingIndex = 0
    
    # brackets
    while startingIndex < len(input):
        if input[startingIndex] == "(":
            result = calc(input[index+1:])
            input = input[0:startingIndex] + result + input[index+1:]
            index = index - (index  - len(result) - startingIndex)
            startingIndex += len(result)
        elif input[startingIndex] == ")":
            startingIndex = len(input)
            index += 1
            break
        index += 1
        startingIndex += 1
    
    # sqrt and to the power of
    ## currently out of order
    """   
    startingIndex = 0
    go = "off"
    while startingIndex < len(input):
        if input[startingIndex] == ")":
            break
        
        if input[startingIndex] == "s":
            if input[startingIndex+1] == "q":
                if input[startingIndex+4] == "-":
                    startingIndex += 1
                    number2="-"
                if go == "on":
                    result = Solver(operator, number2)
                    input = input[0:startingIndex-len(number2)-4] + result + input[startingIndex-len(number2)-4+len(result)]
                elif go == "off":
                    operator = "sqrt"
                    go = "on"
            # TODO elif for sin
        elif input[startingIndex] == "^":
            if go == "on":
                result = Solver("^", number1, number2)
                input = input[0:startingIndex-len(number1)-len(number2)-1] + result + input[startingIndex-len(number1)-len(number2)-1+len(result)]
            if go == "off":
                operator = "^"
                go = "on"
        startingIndex += 1
    if go == "on":
        result = Solver(operator, number1, number2)
        input = input[0:startingIndex-len(number1)-len(number2)-1] + result + input[startingIndex:]

    number1 = ""
    number2 = ""
    
    """
    # multiplication
    
    startingIndex = 0
    go = "off"
    while startingIndex < len(input):
        if input[startingIndex] == ")":
            break
        
        # leading minus
        if (input[startingIndex] == "-" and number1 == "" and number2 == ""):
            number2 += "-"
        # first number
        elif ((input[startingIndex] == "*" or input[startingIndex] == "/") and go == "off"):
            number1 = number2
            number2 = ""
            operator = input[startingIndex]
            go = "on"
        elif ((input[startingIndex] == "*" or input[startingIndex] == "/") and go == "on"):
            input, startingIndex, number1 = inputCutter(input, startingIndex, operator, number1, number2)
            operator = input[startingIndex]
            number2 = ""
        # for *- or /- cases
        elif (input[startingIndex] == "-" and (input[startingIndex-1] == "*" or input[startingIndex-1] == "/") and (startingIndex > 0)):
            number2 += "-"
        elif ((input[startingIndex] == "+" or input[startingIndex] == "-") and go == "on"):
            input, startingIndex, number1 = inputCutter(input, startingIndex, operator, number1, number2)
            number2 = ""
            go = "off"
        elif ((input[startingIndex] == "+" or input[startingIndex] == "-") and go == "off"):
            number2 = ""
        else:
            number2 += input[startingIndex]
        startingIndex +=1
    if go == "on":
        input, startingIndex, number1 = inputCutter(input, startingIndex, operator, number1, number2)

    number1 = ""
    number2 = ""
            
            
    # addition
    for element in input:
        if element == ")":
            break
        elif (element == "-" and number2 == ""):
            number2 += "-"
        elif ((element == "+" or element == "-") and number1 == ""):
            number1 = number2
            number2 = ""
            operator = element
        elif (element == "+" or element == "-"):
            number1 = Solver(operator, number1, number2)
            number2 = ""
            operator = element
        else:
            number2 += element
    if number1 != "" and number2 != "":
        number1 = Solver(operator, number1, number2)
    elif number2 != "":
        number1 = number2
    return number1
        
        
        
print(calc("(3)*4+3"))
index = 0        
print(calc("5*5+5"))
index = 0
print(calc("2*2+2"))
index = 0
print(calc("2+2+(2)"))
index = 0
print(calc("3-2.7*3.456"))
index = 0
print(calc("5*5+3"))
index = 0
print(calc("3+(7*4)+(9+3)"))
index = 0
print(calc("3+6+(7)+(8)"))
index = 0
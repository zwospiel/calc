# sqrt and to the power of
# currently out of order

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
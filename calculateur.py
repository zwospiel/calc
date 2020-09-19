
def calc(string):
    i = 0
    current = 0
    numbers = []
    operators = []
    first_negative = False
    if string == "":
        return("Darn string is empty i tell you what")
    # check for leading negative operator at start
    if string[0] == "-":
        first_negative = True
        string = string[1:]
    # pass so long as we don't encounter an operator; when we do, save the latest number and operator
    # seperately for a clean, neat and organized system, move the "current" pointer up to the newest position
    for element in string:
        if str.isdigit(element):
            pass
        else:
            numbers.append(int(string[current:i]))
            current = i + 1
            if element == "+":
                operators += ("+")
            elif element == "-":
                operators += ("-")
        i += 1
    # adding the last number, because there is no operator at the end
    numbers.append(int(string[current:]))
    
    if first_negative == True:
        numbers[0] = -int(numbers[0])

    result = numbers[0]
    current = 0
    i = len(operators)
    while i > 0:
        if operators[current] == "+":
            result += int(numbers[current+1])
        elif operators[current] == "-":
            result -= int(numbers[current+1])
        current += 1
        i -= 1
    return result


print(calc("3143+5643-555"))
print(calc("17"))
print(calc("-17"))
print(calc("90-45"))
print(calc(""))
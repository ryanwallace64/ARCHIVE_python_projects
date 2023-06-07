def add(n1, n2):
    '''Add two input numbers'''
    return n1 + n2

def subtract(n1, n2):
    '''Subtract two input numbers'''
    return n1 - n2

def multiply(n1, n2):
    '''Multiply two input numbers'''
    return n1 * n2

def divide(n1, n2):
    '''Divide two input numbers'''
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("Enter the first number: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation symbol: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = round(calculation_function(num1, num2), 2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
       
        if input(f"Type 'y' to continue calculationg with {answer}, or type 'n' to exit.: ") == 'n':
            should_continue = False
            calculator()
        else:
            num1 = answer

calculator()
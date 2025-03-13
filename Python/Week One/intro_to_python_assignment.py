# simple python program to ask user input two numbers and perfom operation based on user choice



# perfrom operationbased on user input
def simple_calc():
    # ask input form user
    num1 = float(input('Please enter the first number '))
    num2 = float(input('Please enter the second number '))
    operation = input('Select the operation (+, -, *, /): ')
    # calc operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # check if seocnf num is zero
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Division by zero is not Possible"
    else:
        result = "Invalid operation"

    # Print the result
    print(f"The result of {num1} {operation} {num2} = {result}")

# call function
simple_calc()
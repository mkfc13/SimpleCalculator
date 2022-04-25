def operations(n1, n2, operation):
    if operation == '*':
        return (n1 * n2)
    elif operation == '/':
        return (n1 / n2)
    elif operation =='+':
        return (n1 + n2)
    elif operation =='-':
        return (n1 - n2)

initial_number = float(input("Enter first number: "))
previous_number = initial_number
while True:
        operation = input("Enter operation(+, -, *, /) or Enter/= to end calculation.")
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            new_number = float(input("Enter another number: "))
            result = operations(previous_number, new_number, operation)
            print(previous_number, operation, new_number, "=", result)
            previous_number = result
        elif operation == '=' or operation == '':
            print(f"Your final calculation is {result}")
            break
        else:
            print("I'm new to python, so please only use the listed operation, anything else will get you here. Have a good day.")
            break
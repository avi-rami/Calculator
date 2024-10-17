from art import logo  # Import the calculator art

# Display the calculator art
print(logo)


# Calculator functions
def add(n1, n2):
    """Return the sum of n1 and n2."""
    return n1 + n2


def subtract(n1, n2):
    """Return the result of n1 minus n2."""
    return n1 - n2


def multiply(n1, n2):
    """Return the product of n1 and n2."""
    return n1 * n2


def divide(n1, n2):
    """Return the result of n1 divided by n2."""
    return n1 / n2


# Dictionary to map symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Main loop for the calculator
y_or_n = 'n'
while y_or_n == 'n':
    # Get the first number from the user
    n1 = float(input("What's the first number?: "))

    # Display available operations
    for symbol in operations:
        print(symbol)

    # Loop to perform calculations
    y_or_n = 'y'
    while y_or_n == 'y':
        op_code = input("Pick an operation from the above choices: ")
        n2 = float(input("What's the next number?: "))
        answer = operations[op_code](n1, n2)
        print(f"{n1} {op_code} {n2} = {answer}")
        y_or_n = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculator: ")
        if y_or_n == 'y':
            n1 = answer

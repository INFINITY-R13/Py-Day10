import os

def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def sub(n1, n2):
    """Returns the difference of two numbers."""
    return n1 - n2

def mul(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def div(n1, n2):
    """Returns the division of two numbers. Raises ValueError for division by zero."""
    if n2 == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number(prompt):
    """Prompts the user for a number and handles invalid input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    """Main function to run the calculator."""
    clear_screen()
    print("Welcome to the Python Calculator!")
    
    num1 = get_number("What is your first number?: ")
    
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid operation. Please try again.")
            continue
            
        num2 = get_number("What is your next number?: ")
        
        calculation_function = operations[operation_symbol]
        
        try:
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        except ValueError as e:
            print(e)
            continue

        choice = input(f"Type 'y' to continue with {answer}, or 'n' to start a new calculation: ").lower()
        
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator() # Restart the function for a new calculation

# Start the calculator
calculator()
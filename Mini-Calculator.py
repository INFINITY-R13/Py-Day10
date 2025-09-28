import os

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero!")
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate():
    print("The Python Calculator!")
    
    while True:
        try:
            num1 = float(input("What is your first number?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        for symbol in operations:
            print(symbol)
        
        operation_symbol = input("Pick an operation (or 'q' to quit): ").lower()
        
        if operation_symbol == 'q':
            print("Goodbye!")
            return
        
        if operation_symbol not in operations:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue
        
        try:
            num2 = float(input("What is your next number?: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        try:
            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        except ValueError as e:
            print(e)
            continue
        
        choice = input(f"Type 'y' to continue with {answer}, 'n' to start a new calculation, or 'q' to quit: ").lower()
        
        if choice == 'y':
            num1 = answer
        elif choice == 'q':
            print("Goodbye!")
            return
        else:
            clear_screen()
            print("The Python Calculator!")
            while True:
                try:
                    num1 = float(input("What is your first number?: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

calculate()
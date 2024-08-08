def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
    }

def calculate():
    print("The Python Caculator!")
    should_accumulate = True
    num1 = float(input("What is your first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")    
        num2 = float(input("What is your next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ").lower()

        if choice == "y":
            num1 = answer 
        else:
            should_accumulate = False
            print("\n" * 13)
            calculate()

calculate()



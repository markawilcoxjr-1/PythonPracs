import calc_art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calulator():
    should_accumulate = True

    n1 = float(input("\nEnter first number: \n"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter which mathematical operation you would like to perform '*', '/', '+', '-': \n")
        n2 = float(input("Enter second number: \n"))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 50)
            calulator()

calulator()


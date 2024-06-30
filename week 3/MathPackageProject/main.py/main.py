import sys
import os

# Add the directory containing your package to the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from mymath.addition import add
from mymath.subtraction import subtract
from mymath.multiplication import multiply
from mymath.division import divide
from mymath.modulus import modulus
from mymath.exponentiation import exponentiate
from mymath.square_root import square_root

def get_user_input():
    """
    Gets operation and numbers from the user.
    """
    operation = input("Enter operation (add, subtract, multiply, divide, modulus, exponent, square_root): ").strip().lower()
    if operation == 'square_root':
        a = int(input("Enter the number: "))
        return operation, a, None
    else:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return operation, a, b

def perform_operation(operation, a, b=None):
    """
    Performs the operation based on user input.
    """
    if operation == 'add':
        return add(a, b)
    elif operation == 'subtract':
        return subtract(a, b)
    elif operation == 'multiply':
        return multiply(a, b)
    elif operation == 'divide':
        return divide(a, b)
    elif operation == 'modulus':
        return modulus(a, b)
    elif operation == 'exponentiate':
        return exponentiate(a, b)
    elif operation == 'square_root':
        return square_root(a)
    else:
        print("Invalid operation")
        return None

def main():
    """
    Main function to run the calculator.
    """
    try:
        operation, a, b = get_user_input()
        result = perform_operation(operation, a, b)
        if result is not None:
            print(f"The result of {operation} is: {result}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

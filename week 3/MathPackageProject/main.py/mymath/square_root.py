import math

def square_root(x):
    try:
        if x < 0:
            raise ValueError("Error: Cannot take the square root of a negative number")
        return math.sqrt(x)
    except TypeError:
        print("Error: The argument must be a number")

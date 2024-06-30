def add(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Both arguments must be numbers")

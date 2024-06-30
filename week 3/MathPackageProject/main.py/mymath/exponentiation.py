def exponentiate(base, exponent):
    try:
        return base ** exponent
    except TypeError:
        print("Error: Both arguments must be numbers")

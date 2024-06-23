#Question 2
#Write a code for a function `Is_even(number)` that will:
#1. Takes an integer as an input.
#2. Returns True if the number is even, otherwise False if the number is odd.
#3. Print whether the number was even or odd hint: use conditions

#Code:

def Is_even(number):
    # Check if the number is even
    if number % 2 == 0:
        print(f"The number {number} is even.")
        return True
    else:
        print(f"The number {number} is odd.")
        return False

# Example usage
number = int(input("Enter an integer: "))
result = Is_even(number)
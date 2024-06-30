#Question 4
#Write a code that will:
#1. Contains a function `find_max_min(numbers_list)` that takes a list of numbers and returns both the maximum and minimum numbers in the list.
#2. Prompts the user to enter 5 numbers, stores them in a list, and then uses the `find_max_min` function to find and display the maximum and minimum numbers.

#Code:

def find_max_min(numbers_list):
    # Find the maximum and minimum numbers in the list
    max_number = max(numbers_list)
    min_number = min(numbers_list)
    return max_number, min_number

def main():
    numbers_list = []
    
    # Prompt user to enter 5 numbers
    for i in range(5):
        number = int(input(f"Enter number {i+1}: "))
        numbers_list.append(number)
    
    # Find and display the maximum and minimum numbers
    max_number, min_number = find_max_min(numbers_list)
    print(f"The maximum number is: {max_number}")
    print(f"The minimum number is: {min_number}")

if __name__ == "__main__":
    main()
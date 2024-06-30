#Question 1
#Write a code that will:
#1. Prompt the user to enter their name, age, email, and favorite number.
#2. Stores these inputs in a dictionary with appropriate keys.
#3. Validate the email format (contains "@" and ".").
#4. Displays a message using these variables, formatted as: "Hello [name], you are [age] years old, your email is [email], and your favorite number is [favorite number]."
import re

#function to get input from user
def get_user_input():
    user_info = {}

    # Prompt user for their information
    user_info['name'] = input("Enter your name: ")
    user_info['age'] = input("Enter your age: ")
    user_info['email'] = input("Enter your email: ")
    user_info['favorite_number'] = input("Enter your favorite number: ")
    
    # Function to validate the email format
    def validate_email(email):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email) is not None

    # Validate email
    while not validate_email(user_info['email']):
        print("Invalid email format. Please try again.")
        user_info['email'] = input("Enter your email: ")
    
    return user_info

def display_message(user_info):
    # Display the formatted message
    print(f"Hello {user_info['name']}, you are {user_info['age']} years old, your email is {user_info['email']}, and your favorite number is {user_info['favorite_number']}.")

def main():
    user_info = get_user_input()
    display_message(user_info)

if __name__ == "__main__":
    main()

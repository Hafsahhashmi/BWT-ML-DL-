# Directory: File Handling System
# File: file_handling.py

def read_file(file_path):
    """
    Reads data from a file and prints its contents. Also counts and prints the number of words in the file.
    Handles exceptions for file not found and reading errors.
    """
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File Contents:\n")
            print(contents)
            word_count = len(contents.split())
            print("\nNumber of words in the file:", word_count)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_path}'.")

def write_to_file(file_path, content):
    """
    Writes user input to a file. Handles exceptions related to file writing.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Content successfully written to '{file_path}'.")
    except IOError:
        print(f"Error: An error occurred while writing to the file '{file_path}'.")

def main():
    """
    Main function to demonstrate reading from and writing to files.
    """
    # Read and display the contents of data.txt.txt
    file_path = r"C:\Users\Hafsah\OneDrive\Desktop\Library managment system\data.txt.txt"
    read_file(file_path)
    
    # Get user input and write it to output.txt
    output_path = r"C:\Users\Hafsah\OneDrive\Desktop\Library managment system\output.txt"
    user_input = input("Enter the content you want to write to 'output.txt': ")
    write_to_file(output_path, user_input)

# Run the main function
if __name__ == "__main__":
    main()

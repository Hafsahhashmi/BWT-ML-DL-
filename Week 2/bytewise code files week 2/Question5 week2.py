#Question 5
#Write a code that will:
#1. Prompt the user to enter details of 3 students: name, age, and grade.
#2. Stores these details in a list of tuples, with each tuple containing the name, age, and grade of a student.
#3. Convert this list of tuples into a dictionary with the student name as the key and the tuple (age, grade) as the value.
#4. Displays an appropriate output.

#Code:

def main():
    students_list = []

    # Prompt user to enter details of 3 students
    for i in range(3):
        name = input(f"Enter the name of student {i+1}: ")
        age = int(input(f"Enter the age of student {i+1}: "))
        grade = input(f"Enter the grade of student {i+1}: ")
        students_list.append((name, age, grade))
    
    # Convert the list of tuples into a dictionary
    students_dict = {student[0]: (student[1], student[2]) for student in students_list}
    
    # Display the student details
    print("\nStudent Details:")
    for name, details in students_dict.items():
        print(f"Name: {name}, Age: {details[0]}, Grade: {details[1]}")

if __name__ == "__main__":
    main()
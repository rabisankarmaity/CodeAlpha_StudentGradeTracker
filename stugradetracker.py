# Student Grade Tracker

# Initialize an empty dictionary to store student grades
student_grades = {}

def add_student():
    # Get student name from user
    student_name = input("Enter student name: ")
    student_grades[student_name] = {}
    print(f"Student {student_name} added successfully!")

def add_grade(student_name):
    # Get subject and grade from user
    subject = input("Enter subject: ")
    grade = float(input("Enter grade: "))
    student_grades[student_name][subject] = grade
    print(f"Grade for {subject} added successfully!")

def calculate_average(student_name):
    # Calculate average grade for a student
    total_grade = sum(student_grades[student_name].values())
    average_grade = total_grade / len(student_grades[student_name])
    print(f"Average grade for {student_name}: {average_grade:.2f}")

def display_grades():
    # Display all student grades
    for student, grades in student_grades.items():
        print(f"Grades for {student}:")
        for subject, grade in grades.items():
            print(f"  {subject}: {grade:.2f}")
        print()

while True:
    print("Student Grade Tracker Menu:")
    print("1. Add student")
    print("2. Add grade")
    print("3. Calculate average")
    print("4. Display grades")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        student_name = input("Enter student name: ")
        if student_name in student_grades:
            add_grade(student_name)
        else:
            print("Student not found. Please add student first.")
    elif choice == "3":
        student_name = input("Enter student name: ")
        if student_name in student_grades:
            calculate_average(student_name)
        else:
            print("Student not found. Please add student first.")
    elif choice == "4":
        display_grades()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

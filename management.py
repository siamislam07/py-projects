students = {}

while True:
    print("\nChoose an option:")
    print("1. Add student and grade")
    print("2. View all students and grades")
    print("3. Delete a student")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print("Student added!")

    elif choice == '2':
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")

    elif choice == '3':
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted!")
        else:
            print("Student not found.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please type 1, 2, 3, or 4.")

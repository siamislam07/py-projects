tasks = []

print("Welcome to Simple To-Do App!")

while True:
    print("\nChoose an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

    elif choice == '3':
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted!")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please type 1, 2, 3, or 4.")

tasks = []

while True:
    print("\n--- TODO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, try again")

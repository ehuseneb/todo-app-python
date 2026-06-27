# Todo App with File Saving (Upgraded Version)

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

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
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, try again")

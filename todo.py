# Interactive Todo App (Phone Friendly + Better UI)

tasks = []

print("\n✨ Welcome to Your Todo App ✨")

while True:
    print("\n========================")
    print("📌 TODO MENU")
    print("========================")
    print("1️⃣ Add Task")
    print("2️⃣ View Tasks")
    print("3️⃣ Delete Task")
    print("4️⃣ Exit")
    print("========================")

    choice = input("👉 Choose an option: ")

    if choice == "1":
        task = input("\n✍️ Enter a task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        print("\n📋 Your Tasks:")
        if not tasks:
            print("⚠️ No tasks yet. Add something!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("⚠️ No tasks to delete!")
        else:
            try:
                num = int(input("🗑️ Enter task number to delete: "))
                if 0 < num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"❌ Removed: {removed}")
                else:
                    print("⚠️ Invalid task number")
            except:
                print("⚠️ Please enter a valid number")

    elif choice == "4":
        print("\n👋 Goodbye! Keep building 🚀")
        break

    else:
        print("⚠️ Invalid choice, try again!")

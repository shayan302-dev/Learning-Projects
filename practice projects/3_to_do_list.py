todo_list = []

while True:
    print("\nTo-Do List Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added.")
    
    elif choice == "2":
        if not todo_list:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    
    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Try again.")

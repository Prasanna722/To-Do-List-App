import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # If no file found, start with empty list
    except json.JSONDecodeError:
        return []  # If file is empty or corrupted, start fresh

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Erase Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
            save_tasks(tasks)

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            try:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            try:
                task_index = int(input("Enter the task number to erase: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks.pop(task_index)  # Removes the task at the given index
                    save_tasks(tasks)
                    print("Task erased!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            print("Saving and exiting the To-Do List.")
            save_tasks(tasks)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

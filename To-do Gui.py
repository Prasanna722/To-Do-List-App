import tkinter as tk
from tkinter import messagebox
import json

# Load tasks from the file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Add Task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append({"task": task, "done": False})
        update_task_list()
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Mark Task as Done
def mark_done(index):
    tasks[index]["done"] = True
    update_task_list()
    save_tasks(tasks)

# Erase Task
def erase_task(index):
    tasks.pop(index)
    update_task_list()
    save_tasks(tasks)

# Update the Task List Display
def update_task_list():
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    for idx, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        task_text = f"{task['task']} - {status}"

        task_label = tk.Label(task_list_frame, text=task_text, width=40, anchor="w")
        task_label.grid(row=idx, column=0, sticky="w")

        # Mark Done Button
        if not task["done"]:
            done_button = tk.Button(task_list_frame, text="Mark Done", command=lambda i=idx: mark_done(i))
            done_button.grid(row=idx, column=1)

        # Erase Button
        erase_button = tk.Button(task_list_frame, text="Erase", command=lambda i=idx: erase_task(i))
        erase_button.grid(row=idx, column=2)

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Load tasks
tasks = load_tasks()

# Task Input and Add Button
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Task List Frame
task_list_frame = tk.Frame(root)
task_list_frame.grid(row=1, column=0, columnspan=2, pady=10)

# Initial Task List Update
update_task_list()

# Start the GUI loop
root.mainloop()

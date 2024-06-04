import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("To-Do List")

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    tasks.clear()
    task_listbox.delete(0, tk.END)

# GUI layout
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=35)
task_entry.pack(side=tk.LEFT, padx=10)

add_task_button = tk.Button(frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=10)

clear_tasks_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks)
clear_tasks_button.pack(side=tk.LEFT)

# Run the main application loop
root.mainloop()

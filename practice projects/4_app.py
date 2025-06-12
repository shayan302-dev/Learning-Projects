import tkinter as tk
from tkinter import messagebox

# Window setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Data
to_do_list = []

# Widgets
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

listbox = tk.Listbox(root, width=35, height=10)
listbox.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

# Add Button
add_button = tk.Button(root, text="Add Task")
add_button.pack(pady=5)

# View Button (shows tasks again, but not needed in GUI since Listbox always shows)
view_button = tk.Button(root, text="Refresh Tasks")
view_button.pack(pady=5)

# Remove Button
remove_button = tk.Button(root, text="Remove Task")
remove_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit")
exit_button.pack(pady=5)

# --- Logic directly written here ---

# Add task
def add_task(event=None):
    task = entry.get()
    if task != "":
        to_do_list.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        status_label.config(text="Task Added")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# View task (refresh)
def view_tasks(event=None):
    listbox.delete(0, tk.END)
    if not to_do_list:
        status_label.config(text="No Task Exists")
    else:
        for task in to_do_list:
            listbox.insert(tk.END, task)
        status_label.config(text="Tasks refreshed")

# Remove task
def remove_task(event=None):
    if not to_do_list:
        messagebox.showwarning("Warning", "Nothing to remove")
    else:
        try:
            index = listbox.curselection()[0]
            removed = to_do_list.pop(index)
            listbox.delete(index)
            status_label.config(text=f"Removed: {removed}")
        except IndexError:
            messagebox.showwarning("Selection Error", "Select a task to remove")

# Exit
def exit_program(event=None):
    root.destroy()

# --- Bind buttons ---
add_button.bind("<Button-1>", add_task)
view_button.bind("<Button-1>", view_tasks)
remove_button.bind("<Button-1>", remove_task)
exit_button.bind("<Button-1>", exit_program)

# Run GUI
root.mainloop()

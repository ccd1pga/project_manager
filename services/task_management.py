from services.navigation import main_menu
from models.task import Task
import tkinter as tk
from tkinter import messagebox
from utils.file_io import load_tasks_from_file, save_tasks_to_file

tasks = load_tasks_from_file()

def add_task(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Add new task", font=("Helvetica", 16)).pack(pady=20)

    tk.Label(root, text="Project: ").pack()
    project_entry = tk.Entry(root)
    project_entry.pack()

    tk.Label(root, text="Title: ").pack()
    title_entry = tk.Entry(root)
    title_entry.pack()

    tk.Label(root, text="Details: ").pack()
    details_entry = tk.Entry(root)
    details_entry.pack()

    tk.Label(root, text="Due by: ").pack()
    due_entry = tk.Entry(root)
    due_entry.pack()

    tk.Label(root, text="Assigned to: ").pack()
    assigned_entry = tk.Entry(root)
    assigned_entry.pack()

    tk.Label(root, text="Inform: ").pack()
    inform_entry = tk.Entry(root)
    inform_entry.pack()

    def save_task():
        project = project_entry.get()
        title = title_entry.get()
        details = details_entry.get()
        due = due_entry.get()
        assigned = assigned_entry.get()
        inform = inform_entry.get()

        if project and title and details and assigned and due and inform:
            new_task = Task(project, title, details, assigned, due, inform)
            tasks.append(new_task)
            save_tasks_to_file(tasks)
            messagebox.showinfo("Task has been added to the project.")
            main_menu(root, user, users)
        else:
            messagebox.showwarning("All fields must be complete!")

    tk.Button(root, text="Save task", command=save_task).pack(pady=10)
    tk.Button(root, text="Main menu", command=lambda: main_menu(root, user, users)).pack(pady=10)

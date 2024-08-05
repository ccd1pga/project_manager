import tkinter as tk
from tkinter import messagebox
from models.project import Project, save_projects_to_file, load_projects_from_file


projects = load_projects_from_file() 

def add_project(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Add New Project", font=("Helvetica", 16)).pack(pady=20)
    
    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()
    
    tk.Label(root, text="Description").pack()
    description_entry = tk.Entry(root)
    description_entry.pack()
    
    tk.Label(root, text="Due Date").pack()
    due_date_entry = tk.Entry(root)
    due_date_entry.pack()
    
    tk.Label(root, text="Priority").pack()
    priority_entry = tk.Entry(root)
    priority_entry.pack()

    def save_project():
        name = name_entry.get()
        description = description_entry.get()
        due_date = due_date_entry.get()
        priority = priority_entry.get()
        
        if name and description and due_date and priority:
            new_project = Project(name, description, due_date, priority)
            projects.append(new_project)
            save_projects_to_file()
            messagebox.showinfo("Success", "Project added successfully!")
            main_menu(root, user, users)
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    tk.Button(root, text="Save Project", command=save_project).pack(pady=10)
    tk.Button(root, text="Back to Main Menu", command=lambda: main_menu(root, user, users)).pack(pady=10)


import tkinter as tk
from tkinter import messagebox
import os
from models.project import Project
from utils.file_io import load_projects_from_file, save_projects_to_file
from utils.menu import main_menu

# Load the projects
projects = load_projects_from_file()

def add_project(root, user, users):
    # Clear existing widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    # GUI Layout
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

    # Save project function
    def save_project():
        name = name_entry.get()
        description = description_entry.get()
        due_date = due_date_entry.get()
        priority = priority_entry.get()

        # Load projects from the file
        projects = load_projects_from_file()

        # Check if the project name already exists
        if any(project.name == name for project in projects):
            messagebox.showwarning("Warning", "Project name already exists!")
        else:
            # Create a new project object
            new_project = Project(name, description, due_date, priority)
            projects.append(new_project)
            save_projects_to_file(projects)
            messagebox.showinfo("Success", "Project added successfully!")
            main_menu(root, user, users)

    # Buttons for saving and going back to main menu
    tk.Button(root, text="Save Project", command=save_project).pack(pady=10)
    tk.Button(root, text="Back to Main Menu", command=lambda: main_menu(root, user, users)).pack(pady=10)

import tkinter as tk
from tkinter import messagebox
import project_menu
import task_menu
import user_login import User
import hashlib
import json

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data saved to {filename}")

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            if not data.strip():
                return {}
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def main():
    user_data = load_data('task_manager.json')
    print("User data loaded successfully")
    
    projects_data = load_data('projects.json')
    print("Projects data loaded successfully")

    tasks_data = load_data('tasks.json')
    print("Tasks data loaded successfully")
    
    logged_in_user = None

    while True:
        choice = input("Choose an option: 1. User Login 2. Project Menu 3. Task Menu 4. Exit\n")
        if choice == '1':
            logged_in_user = user_login.login(user_data)
        elif choice == '2':
            if logged_in_user:
                project_menu.manage_projects(logged_in_user, projects_data)
            else:
                print("Please log in first.")
        elif choice == '3':
            if logged_in_user:
                task_menu.manage_tasks(logged_in_user, tasks_data)
            else:
                print("Please log in first.")
        elif choice == '4':
            save_data(user_data, 'task_manager.json')
            save_data(projects_data, 'projects.json')
            save_data(tasks_data, 'tasks.json')
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

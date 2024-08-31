import json
from models.user import User
from models.task import Task
from models.project import Project

# The load and save functions formally in user.py
def load_users_from_file(filename='data/user.json'):
    users = []  # Initialize users as an empty list
    try:
        with open(filename, 'r') as file:
            user_data = json.load(file)
            users = [User.from_dict(data) for data in user_data]
        print("Users loaded from file.")
    except FileNotFoundError:
        print("No saved users found.")
    except json.JSONDecodeError:
        print("Error decoding user file.")
    except Exception as e:
        print(f"An error occurred while loading users from file: {e}")
    return users  # Ensure this always returns a list, even if empty


def save_user_to_file(users, filename='data/user.json'):
    with open(filename, 'w') as file:
        users_data = [user.to_dict() for user in users]
        json.dump(users_data, file)

# The load and save functions formally in task.py
def load_tasks_from_file(filename='data/tasks.json'):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            tasks = [Task(**data) for data in tasks_data]
        print("Tasks loaded from file.")
        return tasks
    except FileNotFoundError:
        print("No saved tasks found.")
    except json.JSONDecodeError:
        print("Error decoding task file.")
    except Exception as e:
        print(f"An error occurred while loading tasks from file: {e}")
    return []


def save_tasks_to_file(tasks, filename='data/tasks.json'):
    try:
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)
            print("Task has been saved.")
    except Exception as e:
        print(f"An error has occurred whilst saving the task: {e}")

# The load and save functions formally in project.py
def save_projects_to_file(projects, filename='data/project.json'):
    try:
        with open(filename, 'w') as f:
            json.dump([project.to_dict() for project in projects], f, indent=4)
            print("Projects have been saved.")
    except Exception as e:
        print(f"An error occurred while saving the project: {e}")

def load_projects_from_file(filename='data/projects.json'):
    try:
        with open(filename, 'r') as file:
            projects_data = json.load(file)
            projects = [Project.from_dict(data) for data in projects_data]
        print("Projects loaded from file.")
        return projects
    except FileNotFoundError:
        print("No saved projects found.")
    except json.JSONDecodeError:
        print("Error decoding project file.")
    except Exception as e:
        print(f"An error occurred while loading projects from file: {e}")
    return []

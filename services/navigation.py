import tkinter as tk
from tkinter import messagebox
from models.user import User  # Ensure this is correct
from tkinter import messagebox
import project_managment as pm
import user_management as um
import task_managment as tm

# These are the functions that move you around the program
def main_menu(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome {user.first_name}!", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(root, text="User Menu", command=lambda: user_menu(root, users)).pack(pady=10)
    tk.Button(root, text="Project Menu", command=lambda: pm.add_project(root, user, users)).pack(pady=10)
    tk.Button(root, text="Logout", command=root.destroy).pack(pady=10)

def user_menu(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="User menu", font=("Helventica", 16)).pack(pady=20)
    tk.Button(root, text="Add project", command=lambda: pm.add_project(root, user, users)).pack(pady=10)
    tk.Button(root, text="Assign task", command=lambda: tm.add_task(root, user, users)).pack(pady=10)
    tk.Button(root, text="Main menu", command=lambda: main_menu(root, user, users)).pack(pady=10)

def show_login(root, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Login", font=("Helvetica", 16)).pack(pady=20) 

    tk.Label(root, text="User_name: ").pack()
    user_name_entry = tk.Entry(root)
    user_name_entry.pack()

    tk.Label(root, text="Password: ").pack()
    password_entry = tk.Entry(root, show='*')
    password_entry.pack()

    def login_user():
        user_name = user_name_entry.get()
        password = password_entry.get()

        for user in users:
            if user.user_name == user_name and user.password_hash == User.hash_password(password):
                main_menu(root, user, users)
                return
                
        messagebox.showerror("Error", "Invalid username or password")

    tk.Button(root, text="Login", command=login_user).pack(pady=20)
    tk.Button(root, text="Register", command=lambda: um.add_user(root, None, users)).pack(pady=10)

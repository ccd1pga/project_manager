# services/shared.py
import tkinter as tk
import services.project_management as pm
import services.user_management as um

def main_menu(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome {user.first_name}!", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(root, text="User Menu", command=lambda: um.user_menu(root, users)).pack(pady=10)
    tk.Button(root, text="Project Menu", command=lambda: pm.add_project(root, user, users)).pack(pady=10)
    tk.Button(root, text="Logout", command=root.destroy).pack(pady=10)
    pass
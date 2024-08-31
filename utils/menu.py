# services/shared.py
import tkinter as tk
from services import project_management as pm
from services import user_management as um
from services import navigation as n

def main_menu(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome {user.first_name}!", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(root, text="User Menu", command=lambda: n.user_menu(root, user, users)).pack(pady=10)
    tk.Button(root, text="Project Menu", command=lambda: pm.add_project(root, user, users)).pack(pady=10)
    tk.Button(root, text="Logout", command=root.destroy).pack(pady=10)
    pass
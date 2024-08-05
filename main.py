import tkinter as tk
from tkinter import messagebox
import services.project_managment as pm

def main_menu(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome {user['first_name']}!", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(root, text="User Menu", command=lambda: show_menu(root)).pack(pady=10)
    tk.Button(root, text="Project Menu", command=lambda: pm.add_project(root, user, users)).pack(pady=10)
    tk.Button(root, text="Logout", command=lambda: show_login(root)).pack(pady=10)

def show_menu(root):
    # Placeholder for user menu functionality
    messagebox.showinfo("Info", "User menu not implemented yet!")

def show_login(root):
    # Placeholder for login functionality
    messagebox.showinfo("Info", "Login not implemented yet!")

def main():
    root = tk.Tk()
    root.title("Project Management System")
    
    user = {'first_name': 'John'}
    users = []

    main_menu(root, user, users)
    
    root.mainloop()

if __name__ == "__main__":
    main()

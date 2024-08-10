import tkinter as tk
from tkinter import messagebox
import services.user_management as um
import services.project_managment as pm
from models.user import load_users_from_file
from services.user_management import show_login

def main_menu(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome {user['first_name']}!", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(root, text="User Menu", command=lambda: um.show_login(root, users)).pack(pady=10)
    tk.Button(root, text="Project Menu", command=lambda: pm.add_project(root, user, users)).pack(pady=10)
    tk.Button(root, text="Logout", command=lambda: main_menu(root, user, users)).pack(pady=10)

def show_menu(root):
    # Placeholder for user menu functionality
    messagebox.showinfo("Info", "User menu not implemented yet!")

def main():
    root = tk.Tk()
    root.title("Project Management System")
    
    users = load_users_from_file()  # Load users list from file
    
    if users:
        show_login(root, users)  # Pass users to the login function
    else:
        print("No users found, cannot proceed to login screen.")
    
    #main_menu(root, users)
    
    root.mainloop()

if __name__ == "__main__":
    main()

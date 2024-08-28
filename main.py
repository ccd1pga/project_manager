import tkinter as tk
from tkinter import messagebox
from utils.file_io import load_users_from_file


def show_menu(root):
    # Placeholder for user menu functionality
    messagebox.showinfo("Info", "User menu not implemented yet!")

def main():
    from services.user_management import first_user
    from services.navigation import show_login
    root = tk.Tk()
    root.title("Project Management System")
    
    users = load_users_from_file()  # Load users list from file
    
    if users:
        show_login(root, users)  # Pass users to the login function
    else:
        first_user(root, users)  # If no users, go to registration screen
    
    root.mainloop()

if __name__ == "__main__":
    main()

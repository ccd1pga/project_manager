import tkinter as tk
from tkinter import messagebox
from models.user import User
from utils.file_io import save_user_to_file
from utils.menu import main_menu

# Use the relative path to import the necessary modules
def add_user(root, user, users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Register", font=("Helvetica", 16)).pack(pady=20)

    tk.Label(root, text="First name: ").pack()
    first_name_entry = tk.Entry(root)
    first_name_entry.pack()

    tk.Label(root, text="Second name: ").pack()
    second_name_entry = tk.Entry(root)
    second_name_entry.pack()

    tk.Label(root, text="User name: ").pack()
    user_name_entry = tk.Entry(root)
    user_name_entry.pack()

    tk.Label(root, text="Email: ").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    tk.Label(root, text="Phone number").pack()
    phone_number_entry = tk.Entry(root)
    phone_number_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show='*')
    password_entry.pack()

    tk.Label(root, text="Re-type password").pack()
    r_password_entry = tk.Entry(root, show='*')
    r_password_entry.pack()

    def save_user():
        first_name = first_name_entry.get()
        second_name = second_name_entry.get()
        user_name = user_name_entry.get()
        email = email_entry.get()
        phone_number = phone_number_entry.get()
        password = password_entry.get()
        r_password = r_password_entry.get()

        if password != r_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        if any(field == '' for field in [first_name, second_name, user_name, email, phone_number, password]):
            messagebox.showerror("Error", "All fields must be filled in.")
            return
        
        new_user = User(first_name, second_name, user_name, email, phone_number, password)
        users.append(new_user)
        save_user_to_file(users)
        messagebox.showinfo("New user registered")
        main_menu(root, new_user, users)

        tk.Label(root, text="Register", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(root, text="Register", command=save_user).pack(pady=20) 

        tk.Button(root, text="Back", command=lambda: main_menu(root, user, users)).pack(pady=10)
        

def first_user(root,users):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Register", font=("Helvetica", 16)).pack(pady=20)

    first_name_entry = tk.Entry(root)
    first_name_entry.pack()
    tk.Label(root, text="First name: ").pack()

    second_name_entry = tk.Entry(root)
    second_name_entry.pack()
    tk.Label(root, text="Second name: ").pack()

    user_name_entry = tk.Entry(root)
    user_name_entry.pack()
    tk.Label(root, text="User name: ").pack()

    email_entry = tk.Entry(root)
    email_entry.pack()
    tk.Label(root, text="Email: ").pack()

    phone_number_entry = tk.Entry(root)
    phone_number_entry.pack()
    tk.Label(root, text="Phone number").pack()

    password_entry = tk.Entry(root, show='*')
    password_entry.pack()
    tk.Label(root, text="Password").pack()

    r_password_entry = tk.Entry(root, show='*')
    r_password_entry.pack()
    tk.Label(root, text="Re-type password").pack()

    def save_first_user():
        first_name = first_name_entry.get()
        second_name = second_name_entry.get()
        user_name = user_name_entry.get()
        email = email_entry.get()
        phone_number = phone_number_entry.get()
        password = password_entry.get()
        r_password = r_password_entry.get()

        if password != r_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        if any(field == '' for field in [first_name, second_name, user_name, email, phone_number, password]):
            messagebox.showerror("Error", "All fields must be filled in.")
            return
        
        new_user = User(first_name, second_name, user_name, email, phone_number, password)
        users.append(new_user)
        save_user_to_file(users)
        messagebox.showinfo("New user registered")
        main_menu(root, new_user, users)

    tk.Button(root, text="Register", command=save_first_user).pack(pady=20)
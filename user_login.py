import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(user_data):
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)

    print(f"Debug: Attempting login for user {username} with hashed password {hashed_password}")

    for user in user_data:
        print(f"Debug: Checking user {user['email']} with stored password {user['password']}")
        if user['email'] == username and user['password'] == hashed_password:
            print("Login successful")
            return user
    print("Invalid username or password")
    return None

import hashlib
import random
import json

class User:
    existing_numbers = set()

    @staticmethod
    def generate_unique_number():
        while True:
            number = random.randint(100, 999)
            if number not in User.existing_numbers:
                User.existing_numbers.add(number)
                return number

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __init__(self, first_name, second_name, user_name, email, phone_number, password, id=None, open_projects=True):
        self.id = id if id is not None else User.generate_unique_number()
        self.first_name = first_name
        self.second_name = second_name
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.password_hash = User.hash_password(password)
        self.open_projects = 'Open Projects' if open_projects else 'No Projects'

    def __repr__(self):
        return (f"User(id={self.id}, first_name='{self.first_name}', second_name='{self.second_name}', "
                f"user_name='{self.user_name}', email='{self.email}', phone_number='{self.phone_number}', "
                f"open_projects='{self.open_projects}')")

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'user_name': self.user_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'password_hash': self.password_hash,
            'open_projects': self.open_projects
        }

    @staticmethod
    def from_dict(data):
        return User(
            first_name=data['first_name'],
            second_name=data['second_name'],
            user_name=data['user_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            password=data['password'],  # Assumes password is provided raw, not hashed
            id=data.get('id'),
            open_projects=data.get('open_projects', 'Open Projects') == 'Open Projects'
        )

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



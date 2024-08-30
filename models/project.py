import random

class Project:
    existing_numbers = set()

    @staticmethod
    def generate_unique_number():
        while True:
            number = random.randint(100, 999)
            if number not in Project.existing_numbers:
                Project.existing_numbers.add(number)
                return number

    def __init__(self, name, description, due_date, priority, status=True, id=None):
        self.id = id if id is not None else Project.generate_unique_number()
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = 'Incomplete' if status else 'complete'
        self.tasks = []

    def __repr__(self):
        return f"Project (id={self.id}, name ={self.name}, description={self.description}, priority={self.priority}, due_date={self.due_date}, status={self.status})"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'status': self.status,
            'task': [task.to_dict() for task in self.tasks]
        }

    @staticmethod
    def from_dict(data):
        return Project(data['name'], data['description'], data['due_date'], data['priority'], data['status'], data['id'])




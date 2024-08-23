class Task:

    def __init__(self, project, title, details, due, assigned, inform):
        self.project = project
        self.title = title
        self.details = details
        self.due = due
        self.assigned = assigned
        self.inform = inform

    def __repr__(self):
        return f"Task (project={self.project}, title={self.title}, details={self.details}, due={self.due}, assigned={self.assigned}, inform={self.inform})"
        
    def to_dict(self):
        return{
            'project': self.project,
            'title': self.title,
            'details': self.details,
            'due': self.due,
            'assigned': self.assigned,
            'inform': self.inform
        }


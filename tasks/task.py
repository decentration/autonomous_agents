import uuid

class Task:
    last_task_number = 0  # Class variable to keep track of the last assigned task number

    def __init__(self, title, description, status, priority, deadline, assignee=None):
        self.id = str(uuid.uuid4())
        # Assign a unique task number and increment the last_task_number
        Task.last_task_number += 1
        self.task_number = Task.last_task_number
        
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.deadline = deadline
        self.assignee = assignee
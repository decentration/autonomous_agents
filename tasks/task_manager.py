from abc import ABC, abstractmethod

class TaskManagerInterface(ABC):
    @abstractmethod
    def add_task(self, task):
        pass

    @abstractmethod
    def remove_task(self, task_id):
        pass

    @abstractmethod
    def get_tasks(self):
        pass

    @abstractmethod
    def update_task_status(self, task_id, new_status):
        pass


class AgileTaskManager(TaskManagerInterface):
    def __init__(self):
        self.tasks = []

    def start_sprint(self, sprint_duration):
        # Implement logic for starting a sprint
        pass

    def end_sprint(self):
        # Implement logic for ending a sprint
        pass

    def add_task_to_backlog(self, task):
        # Implement logic for adding a task to the backlog
        pass

    def move_task_to_sprint(self, task_id):
        # Implement logic for moving a task to a sprint
        pass

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def get_tasks(self):
        return self.tasks

    def update_task_status(self, task_id, new_status):
        # Implement logic for updating the status of a task
        pass

    def sort_tasks(self, key_function):
        self.tasks.sort(key=key_function)


class TeamTaskManager(TaskManagerInterface):
    def __init__(self):
        self.tasks = []

    # Implement the methods from TaskManagerInterface
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def get_tasks(self):
        return self.tasks

    def update_task_status(self, task_id, new_status):
        # Implement logic for updating the status of a task
        pass

    # Add any additional team-specific methods here


class OrganizationTaskManager(TaskManagerInterface):
    def __init__(self):
        self.tasks = []

    # Implement the methods from TaskManagerInterface
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def get_tasks(self):
        return self.tasks

    def update_task_status(self, task_id, new_status):
        # Implement logic for updating the status of a task
        pass

    # Add any additional organization-specific methods here

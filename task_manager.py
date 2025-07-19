import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            completed=data.get("completed", False),
        )

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def search_tasks(self, keyword):
        return [
            task for task in self.tasks
            if keyword.lower() in task.title.lower()
            or keyword.lower() in task.description.lower()
            or keyword in task.due_date
        ]

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                return [Task.from_dict(item) for item in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

import json
import os
import uuid
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, status="pending", task_id=None):
        self.id = task_id or str(uuid.uuid4())[:8]
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data["description"],
            data["due_date"],
            data["status"],
            data["id"]
        )

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()


# === Commit 2 ===
 def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        print("\n📋 Pending Tasks:")
        for task in self.tasks:
            if task.status == "pending":
                self.display_task(task)

        print("\n✅ Completed Tasks:")
        for task in self.tasks:
            if task.status == "completed":
                self.display_task(task)

    def display_task(self, task):
        print(f"ID: {task.id}\n  Title: {task.title}\n  Description: {task.description}\n  Due: {task.due_date}\n  Status: {task.status}\n")

 def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                task_dicts = json.load(f)
                self.tasks = [Task.from_dict(d) for d in task_dicts]


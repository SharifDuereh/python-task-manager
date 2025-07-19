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
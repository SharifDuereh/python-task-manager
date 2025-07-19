def main():
    print("Welcome to Task Manager")

if __name__ == "__main__":
    main()


    # task_manager.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def main():
    while True:
        command = input("Enter command (add/quit): ")
        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        elif command == "quit":
            break

if __name__ == "__main__":
    main()
#3
def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def main():
    while True:
        command = input("Enter command (add/show/quit): ")
        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        elif command == "show":
            show_tasks()
        elif command == "quit":
            break

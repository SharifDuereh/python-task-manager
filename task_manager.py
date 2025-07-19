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

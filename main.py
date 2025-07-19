from task_manager import Task, TaskManager

def print_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

def main():
    manager = TaskManager()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            manager.add_task(task)
            print("✅ Task added!")

        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks found.")
            for i, task in enumerate(tasks):
                status = "✔️" if task.completed else "❌"
                print(f"{i}. [{status}] {task.title} - {task.due_date}")

        elif choice == "3":
            index = int(input("Enter task index to mark complete: "))
            manager.complete_task(index)
            print("✅ Task marked as complete.")

        elif choice == "4":
            index = int(input("Enter task index to delete: "))
            manager.delete_task(index)
            print("🗑️ Task deleted.")

        elif choice == "5":
            keyword = input("Enter keyword or due date: ")
            results = manager.search_tasks(keyword)
            for i, task in enumerate(results):
                status = "✔️" if task.completed else "❌"
                print(f"{i}. [{status}] {task.title} - {task.due_date}")

        elif choice == "6":
            print("👋 Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


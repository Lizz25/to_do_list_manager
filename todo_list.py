class TodoListManager():
    def __init__(self):
        self.task = []

    def add_task(self, task):
        self.task.append({"Title": task, "status": "Pending"})

    def list_task(self):
        return [task["Title"] for task in self.task]
    
    def mark_as_completed(self, task):
        for t in self.task:
            if t["Title"] == task:
                t["status"] = "Completed"

    def clear_tasks(self):
        self.task = []

    def edit_task(self, old_task, new_task, status = "Pending"):
        for t in self.task:
            if t["Title"] == old_task:
                t["Title"] = new_task
                t["status"] = status
    
    def filter_by_status(self, status):
        return [task["Title"] for task in self.task if task["status"] == status]
    
if __name__ == "__main__":
    todo_manager = TodoListManager()
    while True:
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Edit a task")
        print("6. Filter tasks by status")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            todo_manager.add_task(task_description)
        elif choice == "2":
            tasks = todo_manager.list_task()
            if not tasks:
                print("No tasks in the list.")
            else:
                print("Tasks:")
                for task in tasks:
                    print(f"- {task}")
        elif choice == "3":
            task_description = input("Enter task description to mark as completed: ")
            todo_manager.mark_as_completed(task_description)
        elif choice == "4":
            todo_manager.clear_tasks()
            print("All tasks cleared.")
        elif choice == "5":
            old_task = input("Enter task description to edit: ")
            new_task = input("Enter new task description: ")
            status = input("Enter status (Pending/Completed): ")
            todo_manager.edit_task(old_task, new_task, status)
        elif choice == "6":
            status = input("Enter status to filter tasks (Pending/Completed): ")
            filtered_tasks = todo_manager.filter_by_status(status)
            if not filtered_tasks:
                print(f"No {status} tasks in the list.")
            else:
                print(f"{status} Tasks:")
                for task in filtered_tasks:
                    print(f"- {task}")
        elif choice == "7":
            break
        else:
            print("Invalid option. Please select a valid option.")
    
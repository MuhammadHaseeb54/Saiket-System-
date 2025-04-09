# Task 1
# To-Do List Application

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
    def mark_completion(self):
        self.completed = True
    def __str__(self):
        status = "[✓]" if self.completed else "[ ]"
        return f"{status} {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.task_id = 1001

    def add_task(self, description):
        self.tasks[self.task_id] = Task(description)
        print(f"Task added with ID: {self.task_id}")
        self.task_id += 1
    
    def mark_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_completion()
            print("Task marked as completed.")
        else:
            print("Task ID not found.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task_id, task in self.tasks.items():
                print(f"{task_id}: {task}")

def main():
    to_do_list = ToDoList()
    flag = True
    while flag == True: 
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter task description: ")
            to_do_list.add_task(description)
        elif choice == "2":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                to_do_list.mark_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "3":
            to_do_list.view_tasks()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

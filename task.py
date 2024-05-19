class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Task '{description}' added successfully.")

    def mark_task_as_done(self, index):
        if index < len(self.tasks):
            self.tasks[index].status = True
            print(f"Task '{self.tasks[index].description}' marked as done.")
        else:
            print("Invalid task index.")

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status]
        if current_tasks:
            print("Current tasks (not done):")
            for i, task in enumerate(current_tasks):
                print(f"{i+1}. {task.description} - Deadline: {task.deadline}")
        else:
            print("No current tasks.")

# Пример использования
task_manager = TaskManager()

task_manager.add_task("Complete project report", "2022-12-31")
task_manager.add_task("Buy groceries", "2022-12-20")
task_manager.add_task("Call mom", "2022-12-15")

task_manager.mark_task_as_done(1)

task_manager.get_current_tasks()
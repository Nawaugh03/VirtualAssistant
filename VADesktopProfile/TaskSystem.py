class Task:
    def __init__(self, title, desc, priority=1,urgency=1):
        self.Title=title
        self.Desc=desc
        self.priority=priority
        self.urgency=urgency
        self.status= "Pending"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description, priority=1, urgency=1):
        task = Task(name, description, priority, urgency)
        self.tasks.append(task)
        print(f"Task '{name}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}:")
                print(task)

    def update_task(self, task_index, **kwargs):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.name = kwargs.get("name", task.name)
            task.description = kwargs.get("description", task.description)
            task.priority = kwargs.get("priority", task.priority)
            task.urgency = kwargs.get("urgency", task.urgency)
            task.status = kwargs.get("status", task.status)
            print(f"Task {task_index + 1} updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f"Task '{deleted_task.name}' deleted successfully.")
        else:
            print("Invalid task index.")

    def list_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if task.status.lower() == "pending"]
        if not pending_tasks:
            print("No pending tasks.")
        else:
            print("Pending Tasks:")
            for task in pending_tasks:
                print(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].status = "Completed"
            print(f"Task {task_index + 1} marked as completed.")
        else:
            print("Invalid task index.")

if __name__ in '__main__':
    pass
class Task:
    def __init__(self, task_id, title, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.status = status
tasks = []
task_counter = 1
def add_task():
    global task_counter
    title = input("Enter Task Title: ")
    task = Task(task_counter, title)
    tasks.append(task)
    task_counter += 1
    print("✅ Task Added Successfully!\n")
def view_tasks():
    if len(tasks) == 0:
        print("No Tasks Available.\n")
        return
    print("\n===== TASK LIST =====")
    for task in tasks:
        print(f"ID: {task.task_id} | "f"Task: {task.title} | "f"Status: {task.status}")
    print()
def update_task():
    try:
        task_id = int(input("Enter Task ID to Update: "))
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return
    for task in tasks:
        if task.task_id == task_id:
            new_status = input("Enter New Status (Pending/Completed): ")
            task.status = new_status
            print("✅ Task Updated Successfully!\n")
            return
    print("❌ Task Not Found.\n")
def delete_task():
    try:
        task_id = int(input("Enter Task ID to Delete: "))
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("✅ Task Deleted Successfully!\n")
            return
    print("❌ Task Not Found.\n")
while True:
    print("\n" + "=" * 30)
    print("      TASK MANAGER")
    print("=" * 30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice.\n")
tasks = []

def add_task():
    task = input("Please enter a task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' has been added.")
    else:
        print("No task entered.")

def list_tasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index}: {task}")

def delete_task():
    list_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Please enter # to delete a task: "))
        if 0 <= task_index < len(tasks):
            removed = tasks.pop(task_index)
            print(f"Task '{removed}' has been deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input (enter a number).")

if __name__ == "__main__":
    print("Welcome to the to-do list app :)")
    while True:
        print("\nPlease select one of the following options:")
        print("--------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


import os
import csv

TODO_FILE = "todo_list.csv"

# Priority levels (sorted order)
PRIORITY_ORDER = {"High": 1, "Medium": 2, "Low": 3}

# Function to load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                tasks.append({"task": row[0], "priority": row[1], "due_date": row[2]})
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task["task"], task["priority"], task["due_date"]])

# Function to display menu
def display_menu():
    print("\n📌 To-Do List Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Function to display tasks sorted by priority
def display_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    
    # Sorting tasks based on priority
    sorted_tasks = sorted(tasks, key=lambda x: PRIORITY_ORDER[x["priority"]])
    
    print("\n📋 Your Tasks (Sorted by Priority):")
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. [{task['priority']}] {task['task']} - Due: {task['due_date']}")

# Main program loop
tasks = load_tasks()

while True:
    display_menu()
    choice = input("Enter choice: ")

    if choice == "1":  # View tasks
        display_tasks(tasks)

    elif choice == "2":  # Add task
        new_task = input("Enter task description: ")
        
        # Choose priority
        priority = ""
        while priority not in PRIORITY_ORDER:
            priority = input("Enter priority (High, Medium, Low): ").capitalize()

        # Enter due date
        due_date = input("Enter due date (YYYY-MM-DD): ")

        # Add new task
        tasks.append({"task": new_task, "priority": priority, "due_date": due_date})
        save_tasks(tasks)
        print("✅ Task added!")

    elif choice == "3":  # Remove task
        display_tasks(tasks)
        try:
            task_num = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                save_tasks(tasks)
                print(f"❌ Removed task: {removed_task['task']}")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    elif choice == "4":  # Exit program
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please try again.")

import os

FILENAME = "todo.txt"

def add_task(task):
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print(task + " added to the list.")


def view_task():
    try:
        with open(FILENAME, "r") as file:
            task = file.readlines()
            if not task:
                print("Koi task nahi hai")
            for i, task in enumerate(task, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Abhi tak koi task add nahi hua hai.")


def delete_task(task_number):
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number")
            return

        tasks.pop(task_number - 1)

        with open(FILENAME, "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully!")
    except FileNotFoundError:
        print("Koi task list exist nahi karti.")


while True:
    print("\n1. Add Task 2. View Tasks 3. Delete Task 4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_task()
    elif choice == "3":
        view_task()
        num = int(input("Enter task number to delete: "))
        delete_task(num)
    elif choice == "4":
        print("EXITING")
        break
    else:
        print("Invalid choise!")

        
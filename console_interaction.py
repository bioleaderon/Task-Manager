from main import *

def user_menu():
    print('''
1. Add a Task
2. Edit a Task
3. Delete a Task
4. View a Task
5. Save and Exit
    ''')
    try:
        user_willing = int(input("Choose an operation: "))
    except ValueError:
        user_willing = 0

    return user_willing




print("Welcome to Task Manager!")
task_manager = TaskManager()
while True:
    task_manager.save() #auto-saves the program
    user_choice = user_menu()
    if user_choice == 1:
        new_task = Task()
        for task in task_manager.tasks:     #checks if task with the same title exists
            if task.title == new_task.title:
                print("A Task already exists with the same title")
                break
        else:
            task_manager.add(new_task)
    elif user_choice == 2:
        title = input("Enter the title of the task you want to edit: ")
        result = task_manager.find(title)
        if not result:
            print("There is no such a task on the record")
        else:
            for i in form:
                print(i.title())
            ans = input("What would you like to change?\n").lower()
            if ans == "title":
                result.change_title()
            elif ans == "deadline":
                result.change_deadline()
            elif ans == "details":
                result.change_details()
            elif ans == "priority":
                result.change_priority()
            else:
                print("Wrong Input")
    elif user_choice == 3:
        title = input("Enter the title of the task you want to delete: ")
        result = task_manager.find(title)
        if not result:
            print("There is no such a task on the record")
        else:
            task_manager.delete(result)

    elif user_choice == 4:
        title = input("Enter the title of the task you want to view: ")
        result = task_manager.find(title)
        if not result:
            print("There is no such a task on the record")
        else:
            print(result)

    elif user_choice == 5:
        break
    else:
        print("Not valid function")
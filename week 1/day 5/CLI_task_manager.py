tasks = {}

def add_task(tasks):
    new_task = input('Please eneter the new task: ')
    completed = input('Is it completed/uncompleted type y/n: ')

    if completed.lower() == 'y':
        completed = True
    else:
        completed = False


    new_task_id = f'task{len(tasks) + 1}'

    tasks[new_task_id] = {
        'task': new_task,
        'completed': completed
    }

    print('New task added')

def view_tasks(tasks):
    print('Tasks')
    for task_id, task_details in tasks.items():
        print(f"ID: {task_id}, Task: {task_details['task']}, Completed: {task_details['completed']}")

    print('--------')

def update_tasks(tasks):
    task_upadte = input('Please enter the name of the task you wish to change the completion status off: ')

    for task_id, task_details in tasks.items():
        if task_details['task'].lower() == task_upadte.lower():
            status = input('Please enter y for completion or n fot not comleted: ')
            if status.lower() == 'y':
                task_details['completed'] = True
            elif status.lower() == 'n':
                task_details['completed'] = False
            else:
                print('Please enter a y/n')

            return

    print('Task not found!')
                

def delete_task(tasks):
    task_delete = input('Please enter the name of the task that you wish to delete: ')

    for task_id, task_details in tasks.items():
        if task_details['task'].lower() == task_delete.lower():
            tasks.pop(task_id)
            print('Task deleted')
            return

    print('Task not found!')

while True:
    
    print('Press 1 to add a task')
    print('Press 2 to view tasks')
    print('Press 3 to mark task as complete')
    print('Press 4 to delete a task')
    print('press 5 to exit')
    user_choice = input('Please enter your choice: ')

    if user_choice == '1':
        add_task(tasks)
    elif user_choice == '2':
        view_tasks(tasks)
    elif user_choice == '3':
        update_tasks(tasks)
    elif user_choice == '4':
        delete_task(tasks)
    elif user_choice == '5':
        break
    else:
        print('Please enter a valid input!')
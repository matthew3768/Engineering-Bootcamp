
def add_task(): 
    with open('Todo_list.txt', 'a') as file: 
        task = input('Please enter the new task: ')
        file.write(f'{task} \n') 

def view_tasks(): 
    try: 
        with open('Todo_list.txt', 'r') as file: 
            for number, lines in enumerate(file, start=1):
                print(number,'.', lines.strip()) 
    except FileNotFoundError: 
        print('File not found!') 

while True: 
    print('---- TO-DO LIST ----') 
    print('1. Add task') 
    print('2. View task') 
    print('3. Exit') 

    user_choice = input('Please enter your choice: ') 

    if user_choice == '1': 
        add_task() 
    elif user_choice == '2': 
        view_tasks() 
    elif user_choice == '3': 
        print('Have a good rest of your day') 
        break 
    else: 
        print('Please enter a valid input!')

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        

    def display_info(self):
        print('name:', self.name)
        print('salary:£', self.salary)

    

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print('language:', self.programming_language)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print('department:', self.department)

    

employees = []


def add_developer(employees):
    name = input('Name:').strip()

    if name == '':
        print('name cant be empty!')
        return

    try:
        salary = float(input('Salary:£'))
        if salary < 0:
            print('salary cant be negative!')
            return

    except ValueError:
        print('Salary must be a number!')
        return

    programming_language = input('Programing language:')
    if programming_language == '':
        print('Language cant be empty!')
        return

    new_developer = Developer(name, salary, programming_language)
    employees.append(new_developer)
    print('Developer added!')

def add_manager(employees):
    name = input('Name:').strip()

    if name == '':
        print('Name cant be empty!')
        return

    try:
        salary = float(input('Salary:£'))
        if salary < 0:
            print('salary cant be negative')
            return

    except ValueError:
        print('Input has to be a number!')
        return

    department = input('Department:').strip()

    if department == '':
        print('Department cant be empty!')
        return

    new_manager = Manager(name, salary, department)
    employees.append(new_manager)
    print('Manager added!')


def view_employees(employees):
    for employee_number, employee_details in enumerate(employees, start=1):
        print(employee_number,'] -------')
        employee_details.display_info()


def search_employee(employees):
    name = input('Name:').strip()

    for employee_details in employees:
        if employee_details.name.lower() == name.lower():
            print('----------')
            employee_details.display_info()
            return

    print('Employee not found!')


while True:
    print('---- Employee Manager ----')
    print('1. Add developer')
    print('2. Add manager')
    print('3. view employees')
    print('4. search employee')
    print('5. Exit')
    choice = input('Choice:')

    if choice == '1':
        add_developer(employees)
    elif choice == '2':
        add_manager(employees)
    elif choice == '3':
        view_employees(employees)
    elif choice == '4':
        search_employee(employees)
    elif choice == '5':
        print('Have a good rest of your day!')
        break
    else:
        print('Please enter a valid choice')
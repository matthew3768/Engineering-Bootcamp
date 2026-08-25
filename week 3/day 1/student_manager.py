class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print('name: ', self.name)
        print('grade: ', self.grade)

    def has_passed(self):
        if self.grade >= 40:
            print(self.name, 'has passed!')
        else:
            print(self.name, 'has failed!')

students = []

def add_students(students):
    name = input('name: ').strip()

    if name == '':
        print('Name cannot be empty!')
        return
    
    try:
        grade = int(input('grade: '))

        if grade < 0 or grade> 100:
            print('Please enter a grade between 1 and 100!')
            return

    except ValueError:
        print('Please enter a valid number!')
        return


    new_student = Student(name, grade)
    students.append(new_student)
    print('Student added!')

def view_students(students):
    for student_number, student_info in enumerate(students, start=1):
        print(student_number, ')')
        student_info.display_info()
        student_info.has_passed()


while True:
    print('---- Student manager ----')
    print('1. Add student')
    print('2. View student')
    print('3. exit')
    choice = input('Please enter your choice: ')

    if choice == '1':
        add_students(students)
    elif choice == '2':
        view_students(students)
    elif choice == '3':
        print('Have a good rest of your day!')
        break
    else:
        print('Please enter a valid choice!')

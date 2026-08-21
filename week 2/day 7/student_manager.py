import json

def load_students():
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)

        return students
    
    except FileNotFoundError:
        return []

def save_student(students):
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input('name: ').strip()
    try:
        grade = int(input('grade: ').strip())
        if grade < 0 or grade > 100:
            print('Please enter a grade between 1 and 100!')
            return
    except ValueError:
        print('please enter a valid number!')
        return

    new_student = {
        'name': name,
        'grade': grade
    }

    students.append(new_student)
    save_student(students)
    print('student saved!')

def view_students(students):
    for number, student_details in enumerate(students, start=1):
        print(number, ')', '\n', 'name:', student_details['name'], '\n', 'grade:', student_details['grade'])


def search_student(students):
    student_name = input('name: ')

    for student in students:
        if student['name'].lower() == student_name.lower():
            print('name:', student['name'], '\n', 'grade:', student['grade'])
            return
    print('student not found')

def update_student(students):
    name = input('Please enter the name of the student you wish to update: ')

    for student in students:
        if student['name'].lower() == name.lower():
            try:
                grade_update = int(input('please enter the new grade: '))

                if grade_update < 0 or grade_update > 100:
                    print('please enter a grade between 0 and 100!')
                    return

            except ValueError:
                print('Please enter a valid number!')
                return

            student['grade'] = grade_update
            save_student(students)
            print('grade updated!')
            return

    print('Name not found!')


def delete_student(students):
    name = input('Please enter the name of the studnet you widh to delete: ')

    for student in students:
        if student['name'].lower() == name.lower():
            students.remove(student)
            save_student(students)
            print('student deleted!')
            return

    print('student not found')

students = load_students()

while True:
    print('---- Student Manager ----')
    print('1. Add student')
    print('2. view student')
    print('3. search student')
    print('4. update student')
    print('5. delete student')
    print('6. exit')
    choice = input('please enter your choice: ')

    if choice == '1':
        add_student(students)
    elif choice == '2':
        view_students(students)
    elif choice == '3':
        search_student(students)
    elif choice == '4':
        update_student(students)
    elif choice == '5':
        delete_student(students)
    elif choice == '6':
        print('Have a good rest of your day!')
        break
    else:
        print('please enter a valid input!')
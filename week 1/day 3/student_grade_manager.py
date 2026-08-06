student1 = {
    'name': 'Matthew',
    'grade': 67
}

student2 = {
    'name': 'Grace',
    'grade': 78
}

students ={
    'student1': student1,
    'student2': student2
}



def add_student(students):
    new_student_name = input('Please enter the name of the new student: ')
    new_student_grade = int(input('please enter the grade of the new student: '))

    new_student_id = f"student{len(students) + 1}"

    students[new_student_id] = {
        "name": new_student_name,
        "grade": new_student_grade
    }

    print("Student added")

def view_students(students):
    print('List of students:')
    for student_id, student_details in students.items():
        print(f"ID: {student_id}, Name: {student_details['name']}, Grade: {student_details['grade']}")

def update_grade(students):
    student_name = input('please enter the name of the students grade you wish to change: ')

    for student_id, student_details in students.items():
        if student_details['name'].lower() == student_name.lower():
            new_grade = int(input('Please enter the new grade: '))
            student_details['grade'] = new_grade
            print('Grade updated')
            return

    print('Student not found!')

def delete_student(students):
    student_name = input('Please enter the name of the student you want to delete: ')

    for student_id, student_details in students.items():
        if student_details['name'].lower() == student_name.lower():
            students.pop(student_id)
            print('Student deleted')
            return

    print('Student not found!')
        


        







print('Press 1 to add student')
print('Press 2 to view students')
print('Press 3 to update grade')
print('Press 4 to delete student')

while True:

    choice = (input('please enter the number of the option you wish to proceed with: '))

    if choice == '1':
       add_student(students)
    elif choice == '2':
        view_students(students)
    elif choice == '3':
        update_grade(students)
    elif choice == '4':
        delete_student(students)
        

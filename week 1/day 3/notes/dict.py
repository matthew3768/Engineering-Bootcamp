student1 = {
    'name': 'Jhon Doe',
    'course': 'Biology',
    'grade': 'b+',
    'age': 21
}

student2 = {
    'Name': 'Harry Ram',
    'Course': 'Drama',
    'Grade': 'A',
    'Age': 24
}

students = {
    'student1': student1,
    'student2': student2
}

for student_id, student_details in students.items():
    print(student_id, student_details)
    print()

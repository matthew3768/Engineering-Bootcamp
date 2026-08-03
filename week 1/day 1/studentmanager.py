student1 = {
    "Name": "John Smith",
    "Age" : 21,
    "Course" : "Business"
}

student2 = {
    "Name": "Abby Reading",
    "Age" : 19,
    "Course": "Photography"
}
student3 = {
    "Name": "Bobby Clarke",
    "Age": 20,
    "Course": "Engineering"
}

#added 3 students to a nested dictionary
students = {
    "student1": student1,
    "student2": student2,
    "student3": student3
}
print(students)

#add a student 
student4 = {
    "Name": "Harry Ram",
    "Age": 24,
    "Course": "Drama"
}

students["student4"] = student4


print(students)
print(student4.get("Age"))
print(students.get("student3", {}).get("Age", {}))
deleted_student = students.pop("student2")
print(deleted_student)


for student_id, student in students.items():
    print(student_id, student)
    print()

for student_id, student in students.items():
    print(student_id)
    print(f"Name: {student['Name']}")
    print(f"Age: {student['Age']}")
    print(f"Course: {student['Course']}")
    print()
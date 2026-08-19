import csv

with open('students.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)

    for student in reader:
        print(student['name'],'scored:',student['grade'])

with open('students_add.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(["Matthew", 67])


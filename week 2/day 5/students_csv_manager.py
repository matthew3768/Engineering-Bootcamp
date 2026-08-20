import csv

def add_student():
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        name = input('Please enter the name of the student: ')
       
        try:
            grade = int(input('Please enter your grade: '))
            if grade < 0 or grade > 100:
                print('Grade not within 0-100!')
        
            writer.writerow([name, grade])

        except ValueError:
                    print('Please enter a valid number!')

def view_students():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)

        for number, student_details in enumerate(reader,start=1):
            print(number, '.', student_details[0], '-',  student_details[1])

while True:
    print('---- STUDENTS ----')
    print('1. Add students')
    print('2. View students')
    print('3. exit')
    choice = input('Please enter your choice: ')

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        print('Have a good rest of your day!')
        break
    else:
        print('Please enter a valid input!')
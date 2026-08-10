grades = [67, 82, 45, 91, 56, 73, 88, 39]

def display_grades(grades):
    for grade in grades:
        print(f"{grade}")

def calculate_average(grades):
    total = 0
    count = 0
    for grade in grades:
        total += grade
        count += 1

    average_grade = total/count
    print(f'student average grades: {average_grade}')
    
def find_highest_grade(grades):
    highest_grade = grades[0]
    for grade in grades:
        if (grade > highest_grade):
            highest_grade = grade
    print(f'Student highest grade was: {highest_grade}')

def find_lowest_grade(grades):
    lowest_grade = grades[0]
    for grade in grades:
        if (grade < lowest_grade):
            lowest_grade = grade
    print(f'Students lowest grade: {lowest_grade}')

def student_passes(grades):
    pass_count = 0
    for grade in grades:
        if (grade >= 40):
            pass_count += 1
    print(f'number of passes: {pass_count}')

def student_fails(grades):
    fail_count = 0
    for grade in grades:
        if (grade < 40):
            fail_count += 1
    print(f'number of fails: {fail_count}')

def student_grades(grades):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for grade in grades:
        if grade >= 70:
            a += 1
        elif grade >= 60:
            b += 1
        elif grade >= 50:
            c += 1
        elif grade >= 40:
            d +=1
        else:
            e += 1
    print(f'A: {a}')
    print(f'B: {b}')
    print(f'C: {c}')
    print(f'D: {d}')
    print(f'E: {e}')


display_grades(grades)
calculate_average(grades)
find_highest_grade(grades)
find_lowest_grade(grades)
student_passes(grades)
student_fails(grades)
student_grades(grades)

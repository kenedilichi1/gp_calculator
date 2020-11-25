# collect number of subjects offered 
number_of_courses = int(input('Enter the number of subjects offered: '))

course = []
grade = []
units = []

# values for each grade
A = 5
B = 4
C = 3
D = 2
E = 1
F = 0

total_units = sum(units)

# collect the users input(course, unit, grade)
def collect():
    course_conut = 0
    
    while course_conut < number_of_courses:
        get_course = input('Enter course name: ')
        course.append(get_course)
       
        get_units = int(input(f'Enter the unit for {course}: '))
        units.append(get_units)
        
        get_grade = input('Enter your grade: ')
        get_grade = get_grade.upper()
        grade.append(get_grade)
        
        course_conut = course_conut + 1
    result()


# get each unit from the units list
# for u in range(units):




# multiplies the grade points and the course unit of each course
# it provides the result of score / total_units
def result():
    score = 0
    for elements in grade:
        if elements == 'A':
            score = A * units
        elif elements == 'B':
            score = B * units
        elif elements == 'C':
            score = C * units
        elif elements == 'D':
            score = D * units
        elif elements == 'E':
            score = E * units
        elif elements == 'F':
            score = F * units
    
        total_score = sum(score)
        gpa = total_score / total_units
        print(gpa)

collect()

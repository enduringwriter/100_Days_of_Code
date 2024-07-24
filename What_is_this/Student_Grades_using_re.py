# Average Student Grades using re

import re

student_grades_string = input("Input a list, w or w/o brackets \"[...]\", of student grades separarated by a comma ")
# student_grades_string = "90, 80, 70, 88, 72"

# Convert input string to integer list
# list(re.split('[ |, |]+', student_grades_string))
# list(re.split('[ | ]+', student_grades_string.strip('[]')))
student_grades = [int(x) for x in re.split('[ |, |]+', student_grades_string.strip('[]'))]

sum_of_grade_points = 0
number_of_graded_assignments = 0
for x in student_grades:
    sum_of_grade_points += x
    number_of_graded_assignments += 1
average_student_grade = sum_of_grade_points/number_of_graded_assignments
print(f"Average student grade is {average_student_grade}")
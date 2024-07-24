# Student Student Grades Ave Max
# Calculate average student grade and max grade
# User inputs grades separated by a comma "," i.e. 90, 80, 70, 88, 72
# Doesn't work if input is inside of brackets i.e. [90, 80, 70, 88, 72]
# if user is inputing brackets, see file "Student Grads Ave using re"

# Input student grades
student_grades = input("Input a list of student scores separated by a comma ").split(',')
print(student_grades)

# Convert string input to a list of integers
for n in range(0, len(student_grades)):
  student_grades[n] = int(student_grades[n])
print(f"Student grades: {student_grades}")
print(type(student_grades[0]))

# Average grade
sum_of_grade_points = 0
number_of_graded_assignments = 0
for grade in student_grades:
  sum_of_grade_points += grade
  number_of_graded_assignments += 1
average_student_grade = round(sum_of_grade_points/number_of_graded_assignments)
print(f"Sum of grade points = {sum_of_grade_points}")
print(f"Number of graded assignments = {number_of_graded_assignments}")
print(f"Average grade = {average_student_grade}")

# Max grade using max function
print(f"The highest grade the student scored in the class is: {max(student_grades)}")

# Max grade using if condition
max = 0
for grade in student_grades:
    if grade > max:
        max = grade
print(f"The highest grade the student scored in the class is: {max}")

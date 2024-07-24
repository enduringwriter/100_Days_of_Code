# Student Average Grade - no user input; only an array of grades i.e. [90, 80, 70, 88, 72]

student_grades = [90, 80, 70, 88, 72]

sum_of_grade_points = 0
for grade in student_grades:
    sum_of_grade_points += grade
average_student_grade = sum_of_grade_points/len(student_grades)
print(f"Average student grade is {average_student_grade}")

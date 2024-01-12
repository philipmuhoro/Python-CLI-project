def calculate_average_grade(student):
    if student.grades:
        total_grades = sum(grade.value for grade in student.grades)
        average_grade = total_grades / len(student.grades)
        return average_grade
    else:
        return None

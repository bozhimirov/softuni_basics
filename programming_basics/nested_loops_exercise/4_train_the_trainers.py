judges = int(input())
total_grades = 0
total_sum_grades = 0

while True:
    problem_name = input()
    if problem_name == "Finish":
        average_grade = total_sum_grades / total_grades
        print(f"Student's final assessment is {average_grade:.2f}.")
        break
    current_grade_counter = 0
    for x in range(judges):
        grade = float(input())
        total_grades += 1
        total_sum_grades += grade
        current_grade_counter += grade
    current_average_grade = current_grade_counter / judges
    print(f'{problem_name} - {current_average_grade:.2f}.')

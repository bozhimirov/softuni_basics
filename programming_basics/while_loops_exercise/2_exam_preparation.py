problems = int(input())
average_grade = 0
fail = 0
number_of_problems = 0
current_name_of_exam = ""
while True:
    name_of_exam = input()

    if name_of_exam == "Enough":
        print(f"Average score: {average_grade / number_of_problems:.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {current_name_of_exam}")
        break
    number_of_problems += 1
    grade = int(input())
    current_name_of_exam = name_of_exam
    average_grade += grade
    if grade <= 4:
        fail += 1
        if fail == problems:
            print(f"You need a break, {problems} poor grades.")
            break

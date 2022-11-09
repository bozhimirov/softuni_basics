name = input()
current_class = 1
fail = 0

average_grade = 0
while current_class <= 12:
    year_grade = float(input())

    if year_grade < 4:
        fail += 1
        if fail > 1:
            break
    else:
        average_grade += year_grade
        current_class += 1
average_grade_med = average_grade / 12
if current_class == 13:
    print(f"{name} graduated. Average grade: {average_grade_med:.2f}")
else:
    print(f"{name} has been excluded at {current_class} grade ")


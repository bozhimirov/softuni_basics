hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_enter = int(input())
minutes_of_enter = int(input())
status = ""
comment = ""
total_minutes_of_exam = (hour_of_exam * 60) + minutes_of_exam
total_minutes_of_enter = (hour_of_enter * 60) + minutes_of_enter
if (total_minutes_of_exam - 30) <= total_minutes_of_enter <= total_minutes_of_exam:
    status = "On time"
elif total_minutes_of_enter < (total_minutes_of_exam - 30):
    status = "Early"
elif total_minutes_of_enter > total_minutes_of_exam:
    status = "Late"
diff = abs(total_minutes_of_exam - total_minutes_of_enter)
if (total_minutes_of_exam - 60) < total_minutes_of_enter < total_minutes_of_exam:
    comment = (f"{diff} minutes before the start")
elif (total_minutes_of_exam - 60) >= total_minutes_of_enter:
    comment = (f"{diff // 60}:{(diff % 60):02d} hours before the start")
elif (total_minutes_of_exam + 60) > total_minutes_of_enter > total_minutes_of_exam:
    comment = (f"{diff} minutes after the start")
elif (total_minutes_of_exam + 60) <= total_minutes_of_enter:
    comment = (f"{diff // 60}:{(diff % 60):02d} hours after the start")

print(status)
print(comment)

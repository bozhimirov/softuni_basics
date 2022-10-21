
hour = int(input())
minutes = int(input())
new_minutes = minutes + 15
if new_minutes >= 60:
    new_minutes_n = new_minutes % 60
else:
    new_minutes_n = new_minutes
if new_minutes >= 60 and hour == 23:
    hour = 0
elif new_minutes >= 60 and hour < 23:
    hour = hour + 1
print(f'{hour}:{new_minutes_n:02d}')

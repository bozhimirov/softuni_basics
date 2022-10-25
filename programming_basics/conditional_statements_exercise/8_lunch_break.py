import math
movie_name = input()
movie_duration = int(input())
rest_duration = int(input())

lunch_time = rest_duration * 1/8
break_time = rest_duration * 1/4
time_left = rest_duration - lunch_time - break_time
diff = abs(time_left - movie_duration)
if time_left >= movie_duration:
    print(f'You have enough time to watch {movie_name} and left with {math.ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {movie_name}, you need {math.ceil(diff)} more minutes.")

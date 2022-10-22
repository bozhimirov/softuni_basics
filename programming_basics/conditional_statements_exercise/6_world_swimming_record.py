record = float(input())
distance = float(input())
time_for_meter = float(input())
addition = distance // 15
addition_time = addition * 12.5
time_player = time_for_meter * distance + addition_time
seconds_left = abs(record - time_player)
if time_player < record:
    print(f'Yes, he succeeded! The new world record is {time_player:.2f} seconds.')
if time_player >= record:
    print(f'No, he failed! He was {seconds_left:.2f} seconds slower.')

lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())
lenght_dm = lenght / 10
width_dm = width / 10
height_dm = height / 10
volume_liters = lenght_dm * width_dm * height_dm
water_needed = volume_liters - (volume_liters * percent / 100)
print(water_needed)

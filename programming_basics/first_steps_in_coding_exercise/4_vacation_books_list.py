pages = int(input())
read_per_hour = int(input())
days = int(input())
hours_to_read_per_day = (pages // read_per_hour) / days
print(hours_to_read_per_day)

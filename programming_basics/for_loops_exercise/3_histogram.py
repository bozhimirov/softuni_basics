n = int(input())
under_200 = 0
between_200_399 = 0
between_400_599 = 0
between_600_799 = 0
above_800 = 0
for _ in range(n):
    current_number = int(input())
    if current_number < 200:
        under_200 += 1
    elif 200 <= current_number <= 399:
        between_200_399 += 1
    elif 400 <= current_number <= 599:
        between_400_599 += 1
    elif 600 <= current_number <= 799:
        between_600_799 += 1
    else:
        above_800 += 1
print(f"{((under_200 / n) * 100):.2f}%")
print(f"{((between_200_399 / n) * 100):.2f}%")
print(f"{((between_400_599 / n) * 100):.2f}%")
print(f"{((between_600_799 / n) * 100):.2f}%")
print(f"{((above_800 / n) * 100):.2f}%")


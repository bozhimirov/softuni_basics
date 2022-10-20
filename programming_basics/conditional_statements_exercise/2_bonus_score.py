number = int(input())
bonus = 0
if number <= 100:
    bonus = 5
elif 101 < number < 1000:
    bonus = number * 0.2
elif number > 1000:
    bonus = number * 0.1
if number % 2 == 0:
    extra_bonus = 1
elif number % 5 == 0:
    extra_bonus = 2
else:
    extra_bonus = 0
bonus_total = bonus + extra_bonus
print(bonus_total)
print(number + bonus_total)

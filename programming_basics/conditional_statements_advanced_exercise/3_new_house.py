flowers = input()
number = int(input())
budget = int(input())
total = 0
if flowers == "Roses":
    total = number * 5
    if number > 80:
        total = number * 5 - (number * 5 * 0.1)
elif flowers == "Dahlias":
    total = number * 3.8
    if number > 90:
        total = number * 3.8 - (number * 3.8 * 0.15)
elif flowers == "Tulips":
    total = number * 2.8
    if number > 80:
        total = number * 2.8 - (number * 2.8 * 0.15)
elif flowers == "Narcissus":
    total = number * 3
    if number < 120:
        total = number * 3 + (number * 3 * 0.15)
elif flowers == "Gladiolus":
    total = number * 2.5
    if number < 80:
        total = number * 2.5 + (number * 2.5 * 0.2)

diff = abs(total - budget)

if total <= budget:
    print(f"Hey, you have a great garden with {number} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

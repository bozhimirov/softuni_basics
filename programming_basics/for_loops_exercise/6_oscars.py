name = input()
points = float(input())
number_of_assessors = int(input())
total_points = points
for _ in range(number_of_assessors):
    name_assessor = input()
    points_assessor = float(input())
    total_points += ((len(name_assessor)) * points_assessor) / 2
    if total_points > 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {total_points:.01f}!")
        break
diff = abs(total_points - 1250.5)
if total_points < 1250.5:
    print(f"Sorry, {name} you need {diff:.1f} more!")

import math

tours = int(input())
initial_points = int(input())
end_points = initial_points
total_wins = 0
for _ in range(tours):
    count = input()
    if count == "W":
        end_points += 2000
        total_wins += 1
    elif count == "F":
        end_points += 1200
    elif count == "SF":
        end_points += 720
print(f"Final points: {end_points}")
print(f"Average points: {math.floor((end_points - initial_points) / tours)}")
#print(f"Average points: {int((end_points - initial_points) / tours)}")
print(f"{((total_wins / tours) * 100):.2f}%")

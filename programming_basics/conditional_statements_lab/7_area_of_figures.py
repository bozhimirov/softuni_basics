import math
figure = input()
if figure == "square":
    square_side = float(input())
    s = square_side * square_side
    print(f"{s:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    s = side_a * side_b
    print(f"{s:.3f}")
elif figure == "circle":
    radius = float(input())
    s = radius * radius * math.pi
    print(f"{s:.3f}")
elif figure == "triangle":
    side = float(input())
    h = float(input())
    s = side * h / 2
    print(f"{s:.3f}")

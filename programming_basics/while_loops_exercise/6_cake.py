width = int(input())
height = int(input())
number_of_pieces = width * height
reason = False
while number_of_pieces > 0:
    pieces = input()
    if pieces == "STOP":
        reason = True
        break
    else:
        number_of_pieces -= int(pieces)
diff = abs(number_of_pieces)
if reason:
    print(f"{number_of_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")



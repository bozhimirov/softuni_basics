width = int(input())
height = int(input())
length = int(input())
free_space = width * height * length
space_left = False
while free_space > 0:
    boxes = input()
    if boxes == "Done":
        space_left = True
        break
    else:
        free_space -= int(boxes)
if space_left:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")



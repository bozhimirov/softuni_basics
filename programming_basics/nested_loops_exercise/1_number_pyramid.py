number = int(input())
current = 1
condition = False
counter = 1
for row in range(1, number + 1):
    for column in range(1, row + 1):
        if current > number:
            condition = True
            break
        print(current, end=" ")
        current += 1
    if condition:
        break
    print()

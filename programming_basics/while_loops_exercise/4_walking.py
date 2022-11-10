condition = False
total_steps = 0
while True:
    steps = input()

    if steps == "Going home":
        last_steps = int(input())
        total_steps += last_steps

        if total_steps >= 10000:
            condition = True
        break
    total_steps += int(steps)
    if total_steps >= 10000:
        condition = True
        break
diff = abs( total_steps - 10000)
if condition:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

beginning = int(input())
ending = int(input())
magic_number = int(input())
sum_of = 0
combinations = 0
condition = False
for first in range(beginning, ending + 1):
    for second in range(beginning, ending + 1):
        sum_of = first + second
        combinations += 1
        if sum_of == magic_number:
            condition = True
            break
    if condition:
        break
if condition:
    print(f"Combination N:{combinations} ({first} + {second} = {magic_number})")
else:
    print(f"{combinations} combinations - neither equals {magic_number}")

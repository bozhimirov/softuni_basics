import sys

number = input()
max_number = -sys.maxsize
while number != "Stop":
    n = int(number)
    if n > max_number:
        max_number = n
    number = input()
else:
    print(max_number)

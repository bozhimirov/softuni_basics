import sys

number = input()
min_number = sys.maxsize
while number != "Stop":
    n = int(number)
    if n < min_number:
        min_number = n
    number = input()
else:
    print(min_number)

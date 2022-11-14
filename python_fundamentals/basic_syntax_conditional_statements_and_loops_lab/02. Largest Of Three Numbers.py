number_one = int(input())
number_two = int(input())
number_three = int(input())
largest_number = 0
if number_one > number_two:
    largest_number = number_one
else:
    largest_number = number_two
if number_three > largest_number:
    largest_number = number_three
else:
    largest_number = largest_number
print(largest_number)
number = int(input())
#if 100 <= number <= 200 or number == 0:
#    print()
#else:
#    print('invalid')
valid = 100 <= number <= 200 or number == 0
if not valid:
    print('invalid')
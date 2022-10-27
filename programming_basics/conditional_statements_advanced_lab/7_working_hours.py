hour = int(input())
day = input()
working_day = day =="Monday" or day =="Tuesday" or day =="Wednesday" or day =="Thursday" or day =="Friday" \
              or day =="Saturday"
working_hour = 10 <= hour <= 18
if working_hour and working_day:
    print("open")
else:
    print("closed")

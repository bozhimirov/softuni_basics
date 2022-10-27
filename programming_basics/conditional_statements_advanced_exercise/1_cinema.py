projection = input()
row = int(input())
column = int(input())
seats = row * column
total = 0
if projection == "Premiere":
    total = seats * 12
    print(f"{total:.2f} leva")
elif projection == "Normal":
    total = seats * 7.5
    print(f"{total:.2f} leva")
elif projection == "Discount":
    total = seats * 5
    print(f"{total:.2f} leva")

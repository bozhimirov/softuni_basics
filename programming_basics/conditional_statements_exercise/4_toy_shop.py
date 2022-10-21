trip_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minions_count = int(input())
truck_count = int(input())
order_sum = puzzle_count * 2.6 + doll_count * 3 + bear_count * 4.1 \
            + minions_count * 8.2 + truck_count * 2
#print(order_sum)
number_toys = puzzle_count + doll_count + bear_count \
            + minions_count + truck_count
if number_toys >= 50:
    order_sum = order_sum * 0.75
rent = order_sum * 0.1
net_profit = order_sum - rent
diff = abs(net_profit - trip_price)

if net_profit >= trip_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
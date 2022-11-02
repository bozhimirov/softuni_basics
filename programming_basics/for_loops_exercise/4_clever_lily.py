n = int(input())
washing_machine = float(input())
toy_price = int(input())
savings = 0
number_toys = 0
last_year = 0
for year in range(1, n + 1):

    if year % 2 == 0:
        last_year = last_year + 10
        savings += last_year - 1
    else:
        number_toys += 1
money_from_toys = number_toys * toy_price
total_money = savings + money_from_toys
diff = abs(total_money - washing_machine)
if total_money >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

budget = float(input())
n = int(input())
m = int(input())
p = int(input())
price_n = 250 * n
price_m = price_n * 0.35
price_p = price_n * 0.1
total_price = price_n + m * price_m + p * price_p
if n > m:
    total_price -= total_price * 0.15
budget_left = abs(budget - total_price)
if budget >= total_price:
    print(f'You have {budget_left:.2f} leva left!')
if budget < total_price:
    print(f'Not enough money! You need {budget_left:.2f} leva more!')

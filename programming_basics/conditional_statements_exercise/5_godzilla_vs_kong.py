budget = float(input())
statists = int(input())
price_per_statist = float(input())
decor = budget * 0.1
if statists > 150:
    price_per_statist = price_per_statist * 0.9
price_total = decor + (statists * price_per_statist)
money = abs(price_total - budget)
if price_total > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {money:.2f} leva more.')
if price_total <= budget:
    print(f'Action!')
    print(f'Wingard starts filming with {money:.2f} leva left.')

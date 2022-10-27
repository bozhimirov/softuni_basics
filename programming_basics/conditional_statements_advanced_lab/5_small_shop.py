product = input()
town = input()
quantity = float(input())
price = 0
if town == 'Sofia':
    if product == 'coffee':
        price = 0.5
    if product == 'water':
        price = 0.8
    if product == 'beer':
        price = 1.2
    if product == 'sweets':
        price = 1.45
    if product == 'peanuts':
        price = 1.6

elif town == 'Plovdiv':
    if product == 'coffee':
        price = 0.4
    if product == 'water':
        price = 0.7
    if product == 'beer':
        price = 1.15
    if product == 'sweets':
        price = 1.30
    if product == 'peanuts':
        price = 1.5

elif town == 'Varna':
    if product == 'coffee':
        price = 0.45
    if product == 'water':
        price = 0.7
    if product == 'beer':
        price = 1.1
    if product == 'sweets':
        price = 1.35
    if product == 'peanuts':
        price = 1.55

total = quantity * price
print(total)

days = int(input())
type_room = input()
comment = input()
nights = days - 1
price = 0
if type_room == "room for one person":
    price = nights * 18
elif type_room == "apartment":
    price = nights * 25
    if nights < 10:
        price = price - (price * 0.3)
    elif 10 <= nights <= 15:
        price = price - (price * 0.35)
    elif 15 < nights:
        price = price - (price * 0.5)
elif type_room == "president apartment":
    price = nights * 35
    if nights < 10:
        price = price - (price * 0.1)
    elif 10 <= nights <= 15:
        price = price - (price * 0.15)
    elif 15 < nights:
        price = price - (price * 0.2)
if comment == "positive":
    price = price + (price * 0.25)
elif comment == "negative":
    price = price - (price * 0.1)

print(f'{price:.2f}')

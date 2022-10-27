budget = float(input())
season = input()
expences = 0
destination = ()
place = ()
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expences = budget * 0.3
        place = "Camp"
    elif season == "winter":
        expences = budget * 0.7
        place = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expences = budget * 0.4
        place = "Camp"
    elif season == "winter":
        expences = budget * 0.8
        place = "Hotel"
elif 1000 < budget:
    destination = "Europe"
    expences = budget * 0.9
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f'{place} - {expences:.2f}')

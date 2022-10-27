month = input()
nights = int(input())
studio = 0
apartment = 0
if month == "May" or month == "October":
    studio = nights * 50
    apartment = nights * 65
    if 13 > nights > 7:
        studio = studio - (studio * 0.05)
    elif nights > 14:
        studio = studio - (studio * 0.3)
        apartment = apartment - (apartment * 0.1)
elif month == "June" or month == "September":
    studio = nights * 75.2
    apartment = nights * 68.7
    if nights > 14:
        studio = studio - (studio * 0.2)
        apartment = apartment - (apartment * 0.1)
elif month == "July" or month == "August":
    studio = nights * 76
    apartment = nights * 77
    if nights > 14:
        apartment = apartment - (apartment * 0.1)
print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')

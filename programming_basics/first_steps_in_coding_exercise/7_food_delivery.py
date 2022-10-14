chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.4
vegetarian_price = vegetarian_menu * 8.15
meal_price = chicken_price + fish_price + vegetarian_price
dessert_price = meal_price * 0.2
delivery_price = 2.5
total = delivery_price + dessert_price + meal_price
print(total)

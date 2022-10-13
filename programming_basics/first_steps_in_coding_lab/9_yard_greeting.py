square_meters = float(input())
price_for_whole_area = square_meters * 7.61
discount = price_for_whole_area * 0.18
result = price_for_whole_area - discount
print(f'The final price is: {result} lv.')
print(f'The discount is: {discount} lv.')

pencils_count = int(input())
markers_count = int(input())
cleaner_count = int(input())
discount = int(input())
pencils_price = pencils_count * 5.8
markers_price = markers_count * 7.2
cleaner_price = cleaner_count * 1.2
price_total = pencils_price + markers_price + cleaner_price
price_with_discount = price_total - (price_total * (discount/100))
print(price_with_discount)

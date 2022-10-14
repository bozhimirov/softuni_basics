deposit = float(input())
months = int(input())
percent = float(input())

total = deposit + months * ((deposit * (percent/100))/12)
print(total)

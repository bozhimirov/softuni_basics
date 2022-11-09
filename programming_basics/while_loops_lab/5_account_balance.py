command = input()
total_money = 0
while command != "NoMoreMoney":
    sum = float(command)
    if sum < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {sum:.2f}")
        total_money += sum
    command = input()

print(f"Total: {total_money:.2f}")

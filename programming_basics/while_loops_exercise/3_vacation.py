money_needed = float(input())
current_money = float(input())
days = 0
days_for_spending = 0
while current_money < money_needed:
    action = input()
    spend_money = float(input())
    days += 1
    if action == "spend":
        days_for_spending += 1
        if current_money - spend_money < 0:
            current_money = 0
        else:
            current_money -= spend_money
    elif action == "save":
        current_money += float(spend_money)
        days_for_spending = 0

    if days_for_spending == 5:
        print("You can't save the money.")
        print(days)
        break
if current_money >= money_needed:
    print(f"You saved the money for {days} days.")

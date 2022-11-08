while True:
    destination = input()
    if destination == "End":
        break
    minimal_budget = float(input())
    total_sum = 0
    while total_sum < minimal_budget:
        new_sum = float(input())
        total_sum += new_sum
    print(f"Going to {destination}!")


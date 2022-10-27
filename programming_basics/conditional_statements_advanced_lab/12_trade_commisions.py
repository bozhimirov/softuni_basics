town = input()
sales = float(input())
percent = 0
if town == 'Sofia':
    if 0 <= sales <= 500:
        percent = 0.05
        commision = sales * percent
        print(f"{commision:.2f}")
    elif 500 < sales <= 1000:
        percent = 0.07
        commision = sales * percent
        print(f"{commision:.2f}")
    elif 1000 < sales <= 10000:
        percent = 0.08
        commision = sales * percent
        print(f"{commision:.2f}")
    elif sales > 10000:
        percent = 0.12
        commision = sales * percent
        print(f"{commision:.2f}")
    else:
        print('error')

elif town == 'Plovdiv':
    if 0 <= sales <= 500:
        percent = 0.055
        commision = sales * percent
        print(f"{commision:.2f}")
    elif 500 < sales <= 1000:
        percent = 0.08
        commision = sales * percent
        print(f"{commision:.2f}")
    elif 1000 < sales <= 10000:
        percent = 0.12
        commision = sales * percent
        print(f"{commision:.2f}")
    elif sales > 10000:
        percent = 0.145
        commision = sales * percent
        print(f"{commision:.2f}")
    else:
        print('error')

elif town == 'Varna':
    if 0 <= sales <= 500:
        percent = 0.045
        commision = sales * percent
        print(f"{commision:.2f}")
    elif 500 < sales <= 1000:
        percent = 0.075
        commision = sales * percent
        print(f"{commision:.2f}")
    elif 1000 < sales <= 10000:
        percent = 0.1
        commision = sales * percent
        print(f"{commision:.2f}")
    elif sales > 10000:
        percent = 0.13
        commision = sales * percent
        print(f"{commision:.2f}")
    else:
        print('error')

else:
    print('error')


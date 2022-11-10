non_prime_sum = 0
prime_sum = 0
flag = False
while True:
    current_number = input()
    if current_number == "stop":
        break
    current_number = int(current_number)

    if current_number < 0:
        print("Number is negative.")
    else:
        if current_number > 1:
            for i in range(2, current_number):
                if current_number % i == 0:
                    flag = True
                    break
            if flag:
                non_prime_sum += current_number
                flag = False
            else:
                prime_sum += current_number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")

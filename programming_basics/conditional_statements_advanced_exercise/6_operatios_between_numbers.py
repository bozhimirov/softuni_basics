N1 = int(input())
N2 = int(input())
operator = input()
result = 0
check = ()
if operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        check = "even"
    else:
        check = "odd"
    print(f'{N1} + {N2} = {result} - {check}')
if operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        check = "even"
    else:
        check = "odd"
    print(f'{N1} - {N2} = {result} - {check}')
if operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        check = "even"
    else:
        check = "odd"
    print(f'{N1} * {N2} = {result} - {check}')
if operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f'{N1} / {N2} = {result:.2f}')
if operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f'{N1} % {N2} = {result}')

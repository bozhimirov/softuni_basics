n = int(input())
count = 0
for first in range (0, n + 1):
    for second in range(0, n + 1):
        for third in range(0, n + 1):
            if first + second + third == n:
                count += 1
print(count)


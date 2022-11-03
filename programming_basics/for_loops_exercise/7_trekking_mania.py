n = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_climbers = 0
for _ in range(n):
    current_number = int(input())
    total_climbers += current_number
    if current_number <= 5:
        musala += current_number
    elif 6 <= current_number <= 12:
        monblan += current_number
    elif 13 <= current_number <= 25:
        kilimandjaro += current_number
    elif 26 <= current_number <= 40:
        k2 += current_number
    elif current_number >=41:
        everest += current_number
print(f"{((musala / total_climbers) * 100):.2f}%")
print(f"{((monblan / total_climbers) * 100):.2f}%")
print(f"{((kilimandjaro / total_climbers) * 100):.2f}%")
print(f"{((k2 / total_climbers) * 100):.2f}%")
print(f"{((everest / total_climbers) * 100):.2f}%")

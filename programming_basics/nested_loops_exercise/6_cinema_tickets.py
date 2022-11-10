ime_film = input()
student_tickets = 0
standart_tickets = 0
kid_tickets = 0
total_tickets = 0
tickets_per_film = 0
procent_zaetost = 0

while ime_film != "Finish":
    tickets_per_film = 0
    svobodni_mesta = int(input())
    for i in range(svobodni_mesta):
        tip_bilet = input()
        if tip_bilet == 'student':
            student_tickets += 1
        elif tip_bilet == 'standard':
            standart_tickets += 1
        elif tip_bilet == 'kid':
            kid_tickets += 1
        elif tip_bilet == 'End':
            break
        total_tickets += 1
        tickets_per_film += 1
    procent_zaetost = tickets_per_film / svobodni_mesta * 100
    print(f'{ime_film} - {procent_zaetost:.2f}% full.')
    ime_film = input()

print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets * 100):.2f}% student tickets.')
print(f'{(standart_tickets / total_tickets * 100):.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets * 100):.2f}% kids tickets.')

yearly_tax = int(input())
shoes = yearly_tax - (yearly_tax * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes / 4
accessoars = ball / 5
total = yearly_tax + shoes + clothes + ball + accessoars
print(total)

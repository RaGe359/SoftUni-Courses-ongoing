yearly_tax = int(input())

sneakers = yearly_tax - (yearly_tax * 0.4)
outfit = sneakers - (sneakers * 0.2)
ball = outfit * 0.25
accessories = ball * 0.2

total_amount = yearly_tax + sneakers + outfit + ball + accessories

print(total_amount)
groups = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
total_ppl = 0

for i in range(groups):
    people = int(input())

    if people <= 5:
        g1 += people
    elif 5 < people <= 12:
        g2 += people
    elif 12 < people <= 25:
        g3 += people
    elif 25 < people <= 40:
        g4 += people
    else:
        g5 += people

    total_ppl += people

g1 = g1 / total_ppl * 100
g2 = g2 / total_ppl * 100
g3 = g3 / total_ppl * 100
g4 = g4 / total_ppl * 100
g5 = g5 / total_ppl * 100

print(f'{g1:.2f}%')
print(f'{g2:.2f}%')
print(f'{g3:.2f}%')
print(f'{g4:.2f}%')
print(f'{g5:.2f}%')
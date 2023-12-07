budget = float(input())
N = int(input())
M = int(input())
P = int(input())

GPU = N * 250
PC = M * (GPU * 0.35)
RAM = P * (GPU * 0.1)

total = GPU + PC + RAM

if  N > M:
    total = total * 0.85

diff = abs(total-budget)

if total <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
import math

n = int(input())
starting_pts = int(input())

won = 0
pts = 0

for _ in range(n):
    stage = input()

    if stage == "W":
        pts += 2000
        won += 1
    elif stage == "F":
        pts += 1200
    elif stage == "SF":
        pts += 720

pts += starting_pts
avg_pts = (pts - starting_pts) / n
won_percent = won / n * 100

print(f'Final points: {pts}')
print(f'Average points: {math.floor(avg_pts)}')
print(f'{won_percent:.2f}%')
actor = input()
pts = float(input())
n = int(input())

for _ in range(n):
    name = input()
    award = float(input())
    pts += (len(name)* award / 2)

    if pts >= 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {pts:.1f}!")
        break

diff = 1250.5 - pts

if pts < 1250.5:
    print(f"Sorry, {actor} you need {diff:.1f} more!")

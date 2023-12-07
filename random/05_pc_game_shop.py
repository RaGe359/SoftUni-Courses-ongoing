sold_games = int(input())

hearthstone = 0
fortnite = 0
overwatch = 0
others = 0

for _ in range(sold_games):
    game = input()

    if game == "Hearthstone":
        hearthstone += 1
    elif game == "Fornite":
        fortnite += 1
    elif game == "Overwatch":
        overwatch += 1
    else:
        others += 1

hs_pc = hearthstone / sold_games * 100
ft_pc = fortnite / sold_games * 100
ow_pc = overwatch / sold_games * 100
others_pc = others / sold_games * 100

print(f'Hearthstone - {hs_pc:.2f}%')
print(f'Fornite - {ft_pc:.2f}%')
print(f'Overwatch - {ow_pc:.2f}%')
print(f'Others - {others_pc:.2f}%')
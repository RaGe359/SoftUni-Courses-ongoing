
change = float(input())
coins_amt = 0
change_conv = change * 100

while change_conv > 0:
    if change_conv >= 200:
        change_conv -= 200
    elif change_conv >= 100:
        change_conv -= 100
    elif change_conv >= 50:
        change_conv -= 50
    elif change_conv >= 20:
        change_conv -= 20
    elif change_conv >= 10:
        change_conv -= 10
    elif change_conv >= 5:
        change_conv -= 5
    elif change_conv >= 2:
        change_conv -= 2
    elif change_conv >= 1:
        change_conv -= 1
    else:
        break

    coins_amt += 1

print(coins_amt)
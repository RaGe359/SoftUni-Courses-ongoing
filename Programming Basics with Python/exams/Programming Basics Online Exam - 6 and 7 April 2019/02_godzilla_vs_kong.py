budget = float(input())
extras = int(input())
clothes_pp = float(input())

decor = budget * 0.1
clothes = extras * clothes_pp

if extras > 150:
    clothes *= 0.9

total = decor + clothes
diff = abs(budget-total)

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
budget = float(input())
extras = int(input())
clothes_price = float(input())

decor = 0.1 * budget

if extras > 150:
    clothes_price = clothes_price * 0.9

clothes = extras * clothes_price
total_spent = decor + clothes

if total_spent > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_spent-budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget-total_spent:.2f} leva left.")

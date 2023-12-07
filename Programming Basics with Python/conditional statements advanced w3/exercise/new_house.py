type = input()
amt = int(input())
budget = int(input())
total = 0

if type == "Roses":
    if amt > 80:
        total = (amt * 5) * 0.9
    else:
        total = amt * 5
elif type == "Dahlias":
    if amt > 90:
        total = (amt * 3.80) * 0.85
    else:
        total = amt * 3.80
elif type == "Tulips":
    if amt > 80:
        total = (amt * 2.80) * 0.85
    else:
        total = amt * 2.80
elif type == "Narcissus":
    if amt < 120:
        total = (amt * 3) * 1.15
    else:
        total = amt * 3
elif type == "Gladiolus":
    if amt < 80:
        total = (amt * 2.50) * 1.2
    else:
        total = amt * 2.50

diff = abs(budget-total)

if budget >= total:
    print(f"Hey, you have a great garden with {amt} {type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")